#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

//using namespace std;

//Ask user to input their own goal score,
//Explain rules

class dice{

    private:
        int sides,roll;
    public:
        dice(void); //default constructor - side = 6
        dice(int); //parameterized constructor -- passed sides and seeds random num generator.
        int roll_dice(void);//gets a new roll value and returns that value.

};

dice::dice(void) // default constructor - side = 6seeds random num generator
{
    sides=6; //making 6 default
    std::srand(std::time(NULL));

}
dice::dice(int s)//parameterized constructor -- passed sides and seeds random num generator.
{
    sides=s; //making 6 default
    std::srand(std::time(NULL));

}

int dice::roll_dice(void)//gets a new roll value and returns that value.
{
    roll = (std::rand() % sides + 1);
    return roll;
}


class player
{
    private:
        std::string player_name;
        int bank=0;
    public:
        player(void);//default
        player(std::string);//parameterized to set up a human player
        void bank_it(int); // add value to bank
        int get_bank(void); // get the current banked value
        std::string get_name(void); // get the players name
};

player::player(void){
    player_name = "Computer";
    bank = 0; 
}
player::player(std::string S){
    player_name = S;
    bank = 0; 
}
void player::bank_it(int add_it){
    bank = bank + add_it;
}
int player::get_bank(void){
    return bank;

}
std::string player::get_name(void){
    return player_name;
}

int main()
{
 int tmp_total=0;
 int goal = 20 , p_score=0,c_score=0;
 int roll_value=4;//player dice
 bool p_win=0, c_win=0, p_turn=false;  
 std::string choice;

 std::string player_name;
 dice mydice;//default method
 //dice mydice(6);//param method

 std::cout << "Explain Rules" << std::endl;

 player computerplayer;
 player_name = "Default"; // replace later with user input
 player my_player(player_name);

 //p_score=0; //replace later init with player class
 roll_value=mydice.roll_dice();//player dice
 
 //outer do until someone wins
 do{
     //players turn
     p_turn=true;
     tmp_total = 0 ;
     do {

     roll_value=mydice.roll_dice();//player dice
     std::cout<< "Player " << my_player.get_name() << " you rolled " << roll_value <<std::endl;

     if(roll_value > 1){
         tmp_total = tmp_total + roll_value;
         std::cout << "Your temporary total is "<< tmp_total <<std::endl;
         std::cout << "Your banked total is "<< my_player.get_bank() <<std::endl;
         std::cout << "Do you want to roll again? Y or N "<<std::endl;
         std::cin >> choice ; 
         if (choice == "Y"){
             std::cout << "You selected to roll again "<<std::endl;
             p_turn = true;

         }
         else{
             p_turn = false;
             //p_score = p_score + tmp_total;
             my_player.bank_it(tmp_total);
             tmp_total=0;
         }
     }
     //lose turn
     else {
         std::cout << "You lose your turn because you rolled a 1"<< std::endl;
         tmp_total=0;
         p_turn=false;
     }//end of players turn
 }while(p_turn);
     if(my_player.get_bank() >= goal){  
         p_win=true;
    }
    else{
        //computers turn
        tmp_total=0;
        roll_value=mydice.roll_dice();
        std::cout<< "Computer rolled " << roll_value <<std::endl;
        tmp_total = roll_value;
        if (roll_value > 1){
            //c_score = c_score + tmp_total;
            computerplayer.bank_it(tmp_total);
            tmp_total=0;
            if(computerplayer.get_bank()>=goal) c_win;
            
        }
        else{
            std::cout << "Computer lost because it rolled a 1 "<<std::endl;
        }
    }
 }while(!p_win && !c_win);
 
 if (p_win){
     std::cout << "Player, "<< my_player.get_name()<< ", you won!"<<std::endl;
 }
 else{
     std::cout << "Player, "<< computerplayer.get_name()<< ", you won!"<<std::endl;
 }
 return 0;
}