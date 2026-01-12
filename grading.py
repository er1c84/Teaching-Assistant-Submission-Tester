import subprocess

programs = ["lab5.c"]
executables = ["lab5"]

#loops through the each program in list#
#this runs gcc lab5.c -o lab5 in C
for i, program in enumerate(programs):
    compile_process = subprocess.run(
        ["gcc", program, "-o", executables[i]],
        capture_output=True,
        text=True
    )

    if compile_process.returncode != 0:
        print(f"Compilation Failed for {program}!")
        print(compile_process.stderr)  # Print error messages
        exit(1)
    
    if compile_process.stderr:
        print(f"Warnings during compilation of {program}:")
        print(compile_process.stderr)
    else:
        print(f"Compilation successful for {program}!")

print("Compilation successful!\n")

### TESTING lab5.c ###
print("Testing lab5...\n")

# Run the compiled program and pass input if needed
# Run compiled program ./lab5 with input customer_data.txt
process = subprocess.run(
    ["./lab5", "customer_data.txt"],
    capture_output=True,
    text=True
)

# Get the output
output_text = process.stdout.strip()
expected = "Item: Cream Quantity: 12 Item Cost: $ 1.39 Subtotal: $ 16.68\nItem: Sorbet Quantity: 17 Item Cost: $ 5.40 Subtotal: $ 91.80\nItem: Cookies Quantity: 40 Item Cost: $ 3.89 Subtotal: $ 155.60\nItem: Vinegar Quantity: 5 Item Cost: $ 3.29 Subtotal: $ 16.45\nItem: Beef Quantity: 4 Item Cost: $ 10.79 Subtotal: $ 43.16\nItem: Avocado Quantity: 40 Item Cost: $ 0.79 Subtotal: $ 31.60\nItem: Celery Quantity: 30 Item Cost: $ 1.98 Subtotal: $ 59.40\nItem: Brocoli Quantity: 34 Item Cost: $ 1.89 Subtotal: $ 64.26\nItem: Spinach Quantity: 20 Item Cost: $ 1.49 Subtotal: $ 29.80\nItem: Garlic Quantity: 27 Item Cost: $ 0.99 Subtotal: $ 26.73\nItem: Mushrooms Quantity: 5 Item Cost: $ 3.78 Subtotal: $ 18.90\nItem: Potatoes Quantity: 11 Item Cost: $ 5.99 Subtotal: $ 65.89\nItem: Carrots Quantity: 14 Item Cost: $ 1.99 Subtotal: $ 27.86\n-----------------------------------------------------\nTotal Items: 13 Total Cost: $648.13\n"

print(f"Test 1: Got:\n{output_text}\n\nExpected:\n{expected}")
