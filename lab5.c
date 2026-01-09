#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 100

// Function to print each item/ pretty print 
void pretty_print(char item[], int quantity, float cost) {
    float subtotal = quantity * cost;
    printf("Item: %s Quantity: %d Item Cost: $ %.2f Subtotal: $ %.2f\n",
           item, quantity, cost, subtotal);
}

// parse one line and subtotal
float parse_data(char line[]) {
    char item[50];
    int quantity;
    float cost;

    sscanf(line, "%s %d %f", item, &quantity, &cost);
    pretty_print(item, quantity, cost);

    return quantity * cost;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: ./lab5 <filename>\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        printf("Unable to open the input file.\n");
        return 1;
    }

    char line[MAX_LINE];
    int total_items = 0;
    float total_cost = 0.0;

    while (fgets(line, sizeof(line), file)) {
        total_cost += parse_data(line);
        total_items++;
    }

    fclose(file);

    printf("-----------------------------------------------------\n");
    printf("Total Items: %d Total Cost: $%.2f\n", total_items, total_cost);

    return 0;
}