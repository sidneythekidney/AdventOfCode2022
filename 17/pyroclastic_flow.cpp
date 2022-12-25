#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

const int NUMBER_OF_ROCKS_PLACED = 50;
const int NUMBER_OF_TYPES_OF_ROCKS = 5;
const int MAX_ROCK_HEIGHT = 8088;
const int CHAMBER_WIDTH = 7;
const int ROCK_STARTING_COLUMN = 2;
const int ROCK_STARTING_ROW_ABOVE_HIGHEST_ROCK = 3;

/*
    General strategy
        - Keep track of coordinates for whatever rock is falling
        - Every time the rock drops, check bottom coordinates below and update all coordinates
        - Every time the rock is blown left, check left-most coordinates, vice versa for right
        - Indicators
            - 0: empty square
            - 1: rock falling
            - 2: fallen rock
        - Iterate over the 2022 turns necessary, simulate falling and jet flow of rocks interchangeably
        - Tallest possible stack of rocks: 2022 * 4 = 8088
*/

/*
    Rock struct
        - Coordinate offsets
        - bottom-most coordinate offsets
        - left-most coordinate offsets
        - right-most coordinate offsets
*/

// Utility functions
template <class T>
void print_2d_vector(vector<vector<T>> vector_2d)
{
    for (auto vector_1d : vector_2d)
    {
        for (auto ele : vector_1d)
        {
            cout << ele << " ";
        }
        cout << "\n";
    }
}

enum ChamberSpace
{
    Occupied = '#',
    Falling = '@',
    Empty = '.',
};

class Rock
{
    public:
        Rock(vector<vector<int>> offsets)
        {
            _offsets = offsets;
            _left_offsets = {};
            _right_offsets = {};
            _bottom_offsets = {};

            _height = 0;

            // Determine left, right , and, bottom offsets
            map<int, int> min_col_by_row = {};
            map<int, int> max_col_by_row = {};
            map<int, int> max_row_by_col = {};

            for (auto offset : offsets)
            {
                // offset in {row, col} format
                int row = offset[0];
                int col = offset[1];

                if (row > _height)
                {
                    _height = row;
                }

                // min_col_by_row
                if (min_col_by_row.find(row) != min_col_by_row.end())
                {
                    if (min_col_by_row[row] > col)
                    {
                        min_col_by_row[row] = col;
                    }
                }
                else
                {
                    min_col_by_row[row] = col;
                }

                // max_col_by_row
                if (max_col_by_row.find(row) != max_col_by_row.end())
                {
                    if (max_col_by_row[row] < col)
                    {
                        max_col_by_row[row] = col;
                    }
                }
                else
                {
                    max_col_by_row[row] = col;
                }

                // max_row_by_col
                if (max_row_by_col.find(col) != max_row_by_col.end())
                {
                    if (max_row_by_col[col] < row)
                    {
                        max_row_by_col[col] = row;
                    }
                }
                else
                {
                    max_row_by_col[col] = row;
                }
            }

            for (auto offset : offsets)
            {
                // offset in {row, col} format
                int row = offset[0];
                int col = offset[1];

                // Add entries to left most offset
                if (col == min_col_by_row[row])
                {
                    _left_offsets.push_back(offset);
                }

                // Add entries to right most offset
                if (col == max_col_by_row[row])
                {
                    _right_offsets.push_back(offset);
                }

                // Add entries to bottom most offset
                if (row == max_row_by_col[col])
                {
                    _bottom_offsets.push_back(offset);
                }
            }
        }

        vector<vector<int>> _offsets;
        vector<vector<int>> _left_offsets;
        vector<vector<int>> _right_offsets;
        vector<vector<int>> _bottom_offsets;

        int _height;
};

/*
    Rock picker class:
        - Keeps track of the next rock
        - Keeps track of the current rock count
*/

class RockPicker
{
    public:
        // Constructor
        RockPicker()
        {
            // Add rocks to all_rocks vector
            vector<vector<int>> rock_1_offsets = {
                // row, col
                {0, 0},
                {0, 1},
                {0, 2},
                {0, 3},
            };
            vector<vector<int>> rock_2_offsets = {
                // row, col
                {0, 1},
                {1, 0},
                {1, 1},
                {1, 2},
                {2, 1},
            };
            vector<vector<int>> rock_3_offsets = {
                // row, col
                {0, 2},
                {1, 2},
                {2, 2},
                {2, 1},
                {2, 0},
            };
            vector<vector<int>> rock_4_offsets = {
                // row, col
                {0, 0},
                {1, 0},
                {2, 0},
                {3, 0},
            };
            vector<vector<int>> rock_5_offsets = {
                // row, col
                {0, 0},
                {0, 1},
                {1, 0},
                {1, 1},
            };

            _all_rocks = {};
            _all_rocks.emplace_back(Rock(rock_1_offsets));
            _all_rocks.emplace_back(Rock(rock_2_offsets));
            _all_rocks.emplace_back(Rock(rock_3_offsets));
            _all_rocks.emplace_back(Rock(rock_4_offsets));
            _all_rocks.emplace_back(Rock(rock_5_offsets));

            _current_rock = 0;
            _rocks_placed = 0;
        }

        // Member functions
        Rock get_current_rock()
        {
            Rock to_return = _all_rocks[_current_rock];
            // Update current rock
            if (++_current_rock == _all_rocks.size())
            {
                _current_rock = 0;
            }
            return to_return;
        }

        // Member variables
        vector<Rock> _all_rocks;
        int _current_rock;
        int _rocks_placed;
};

/*
    Chamber class:
        - Keep track of the rocks in the chamber using the indicators above
        - Reach out to rock picker class to track which one is falling
        - Simulate falling of the rock
        - Simulate jetflow and effect on the rocks
*/

class Chamber
{
    public:
        // Constructor
        Chamber(string jet_flow) : _jet_flow(jet_flow), _jet_flow_current_idx(0), _max_height_of_placed_rocks(0), _current_rock(Rock({}))
        {
            // Create the chamber
            _chamber_state = vector<vector<char>>(MAX_ROCK_HEIGHT, vector<char>(CHAMBER_WIDTH, Empty));
            _rock_picker = RockPicker();
        }

        // Member functions
        void move_rock_left()
        {
            // Check collisions to the left
            int start_row = _current_rock_position[0];
            int start_col = _current_rock_position[1];

            for (auto left_rock : _current_rock._left_offsets)
            {
                int row = left_rock[0];
                int col = left_rock[1];
                if ((start_col + col) == 0 || _chamber_state[start_row + row][start_col + col - 1] != Empty)
                {
                    return;
                }
            }
            // Once we reach this point the rocks can move left
            _current_rock_position[1] -= 1;
        }

        void move_rock_right()
        {
            // Check collisions to the right
            int start_row = _current_rock_position[0];
            int start_col = _current_rock_position[1];

            for (auto right_rock : _current_rock._right_offsets)
            {
                int row = right_rock[0];
                int col = right_rock[1];
                if ((start_col + col) == 0 || _chamber_state[start_row + row][start_col + col + 1] != Empty)
                {
                    return;
                }
            }
            // Once we reach this point the rocks can move right
            _current_rock_position[1] += 1;
        }

        bool move_rock_down()
        {
            cout << "Moving rock down\n";
            // Check collisions to the down
            int start_row = _current_rock_position[0];
            int start_col = _current_rock_position[1];

            for (auto bottom_rock : _current_rock._bottom_offsets)
            {
                int row = bottom_rock[0];
                int col = bottom_rock[1];
                if ((start_row + row + 1 == MAX_ROCK_HEIGHT) || _chamber_state[start_row + row + 1][start_col + col] != Empty)
                {
                    // Place rock and exit function if rock cannot move anymore
                    _max_height_of_placed_rocks = max(_max_height_of_placed_rocks, MAX_ROCK_HEIGHT - _current_rock_position[0]);
                    place_current_rock();
                    return false;
                }
            }
            // Once we reach this point the rocks can move down
            _current_rock_position[0] += 1;

            return true;
        }

        void get_new_rock()
        {
            _current_rock = _rock_picker.get_current_rock();
            // Set initial position of the rock
            int starting_row = MAX_ROCK_HEIGHT - 1 - _max_height_of_placed_rocks - ROCK_STARTING_ROW_ABOVE_HIGHEST_ROCK - _current_rock._height;
            _current_rock_position = {starting_row, ROCK_STARTING_COLUMN};
        }

        void place_current_rock()
        {
            int starting_row = _current_rock_position[0];
            int starting_col = _current_rock_position[1];

            for (auto offset : _current_rock._offsets)
            {
                int row = offset[0];
                int col = offset[1];
                _chamber_state[starting_row + row][starting_col + col] = Occupied;
            }
        }

        void print_chamber()
        {
            // Debug function
            // Create a new vector representing the chamber
            cout << "Printing chamber:\n";
            int start_row = _current_rock_position[0];
            int start_col = _current_rock_position[1];

            vector<vector<char>> chamber = {};
            for (int i = start_row; i < MAX_ROCK_HEIGHT; ++i)
            {
                chamber.push_back(_chamber_state[i]);
            }
            // Add in the falling rocks
            for (auto offset : _current_rock._offsets)
            {
                int row = offset[0];
                int col = offset[1];
                chamber[row][start_col + col] = Falling;
            }
            
            // Print entire relevant parts of the chamber 
            for (int i = 0; i < chamber.size(); ++i)
            {
                for (int j = 0; j < CHAMBER_WIDTH; ++j)
                {
                    // Print the piece falling as well
                    cout << chamber[i][j] << " ";
                }
                cout << "\n";
            }
            cout << "\n\n";
        }

        char get_jet_flow_movement()
        {
            char to_return = _jet_flow[_jet_flow_current_idx];
            // Update _jet_flow_current_idx
            if (++_jet_flow_current_idx == _jet_flow.length())
            {
                _jet_flow_current_idx = 0;
            }

            return to_return;
        }

        void move_rock_by_jetstream_flow()
        {
            char jet_flow_movement = get_jet_flow_movement();
            
            if (jet_flow_movement == '<')
            {
                cout << "Moving rock left\n";
                move_rock_left();
            }
            else
            {
                cout << "Moving rock right\n";
                move_rock_right();
            }
        }

        void simulate_chamber()
        {
            // Loop over all rocks
            for (int i = 0; i < NUMBER_OF_ROCKS_PLACED; ++i)
            {
                cout << "Simulating rock number: " << i + 1 << "\n";
                // For each rock, alternate between moving the rock down and moving the rock left/right depending on the jetstream
                get_new_rock();
                do
                {
                    //print_chamber();
                    move_rock_by_jetstream_flow();
                } while(move_rock_down());
            }
        }

        // Member variables
        string _jet_flow;
        int _jet_flow_current_idx;
        vector<vector<char>> _chamber_state;
        RockPicker _rock_picker;
        Rock _current_rock;
        vector<int> _current_rock_position;
        int _max_height_of_placed_rocks;
};


int main()
{
    ifstream jetflow_file("./jetflow_sample.txt");

    string jetflow_text;
    string jetflow = ""; 

    while (getline(jetflow_file, jetflow_text))
    {
        jetflow += jetflow_text;
    }

    RockPicker rock_picker = RockPicker();

    Chamber chamber = Chamber(jetflow);

    chamber.simulate_chamber();

    cout << "Max height of rocks: " << chamber._max_height_of_placed_rocks << "\n";

    //Quick test:
    // for (int i = 0; i < NUMBER_OF_TYPES_OF_ROCKS; ++i)
    // {
    //     cout << "Rock " << i+1 << ":\n";
    //     Rock current_rock = rock_picker.get_current_rock();

    //     // printing offsets
    //     cout << "all offsets:\n";
    //     print_2d_vector(current_rock._offsets);
    //     cout << "left offsets:\n";
    //     print_2d_vector(current_rock._left_offsets);
    //     cout << "right offsets:\n";
    //     print_2d_vector(current_rock._right_offsets);
    //     cout << "bottom offsets:\n";
    //     print_2d_vector(current_rock._bottom_offsets);
    // }


}
