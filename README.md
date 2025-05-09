#  Phantasmal Force 🐍🌀
Some python scripts to make inventory management a certain vendor slightly? less painful.

## Set up your python virtual environment 

Create it:
```
python3 -m venv venv
```

Activate it
```
source venv/bin/activate
```

## Update Local Library
You are going to export a copy of our current library and save it to the project directory

- Go to Items → Action → Export
- Save it in this directory as 'currentcat.csv'
- Replace existing file → yes

## Get Order Details
Copy order details from the vendor website into 'data.txt'. It will look like this, only much much much longer.

```
6056133005249       | * Item 1* GTIN
I AM A FAKE ITEM    | * Item 1* Name
1                   | * Item 1* Qty Ordered
$9.80               | * Item 1* Unit Cost
$9.80               | * Item 1* Order Total
5706569110123       | * Item 2 * GTIN
FAKE ITEM #2        | * Item 2 * Item Name
2                   | * Item 2 * Qty Ordered
$9.20               | * Item 2* Unit Cost
$18.40              | * Item 2* Order Total
```

## Create and compare CSV files

Create a spreadsheet for the order

```
py minor-illusion.py
```

Compare GTIN against existing library
```
py compare-gtin.py
```

This will generate 'new_items.csv'

## Purchase Order Template
- Open your spreadsheet application of choice 
- Open 'new_items.csv' and 'library_template.xlsx' from the project directory

Note: The version included in this repo has some custom formatting to make your life easier

## Duplicate and Update Library Template 
*Before you start working*
- Duplicate the template and give it a useful name
- Save to a different location (shared drives are good) and work from there 

### Adding New Item Data
Now you are going to add the new items to the duplicate template you just created.  
- Open 'new_items.csv'
- Starting at row 2, copy the 'Item Name' Column from 'new_items.csv'
- Paste into your template using 'Paste and match style'
- Repeat for GTIN and Unit Cost 

*Note: GTIN must be formatted as 'text'*

### Pricing
Once you have added Item Name, GTIN and Unit Costs, you need to add price
- Sort the template by ascending unit cost
- Use standard pricing practices 

### Finish the Template
- Ensure all of the yellow columns are filled in: Reporting Category, Default Vendor Name, Tax
- Tax should be 'Y' in everything except for books
- Export the finished template to .xlsx file


### Import Template
- Import your freshly exported and updated template using
- DO NOT OVERWRIGHT THE ENTIRE EXISTING LIBRARY OR YOU WILL HAVE A BAD TIME 