#include <stdio.h>

int main() {
    int choice, quantity;
    float prices[]={30, 60, 80};
    float bill=0;
    
    printf("============\n");
    printf("MY G-Shop\n");
    printf("============\n");
    while(1){
        printf("Item     Unit    Price (Tk)\n");
        printf("=======  =====   ===========\n");
        printf("1. Potato  1 Kg   30\n");
        printf("2. Tomato  1 Kg   60\n");
        printf("3. Onion   1 Kg   80\n");
        printf("4. Exit\n");

        printf("Enter Your Choice: ");
        scanf("%d",&choice);
        if(choice==4) {
            break;
        }
        if(choice<1 || choice>4) {
            printf("Invalid choice. Please try again.\n");
            continue;
        }
        printf("How much do you want to buy (in Kg): ");
        scanf("%d",&quantity);

        if(quantity<=0) {
            printf("Invalid quantity. Please try again.\n");
            continue;
        }

        bill +=prices[choice-1]*quantity;
        printf("Your current bill is : %.2f (Tk.)\n", bill);
    }

    printf("Your Final Bill is : %.2f (Tk.)\n", bill);

    return 0;
}