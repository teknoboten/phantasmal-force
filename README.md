#  Phantasmal Force 🐍🌀
Some python scripts to make inventory management a certain vendor slightly? less painful. Assuming you have knowledge and access to do the things. 

## Set up your python virtual environment 

```zsh
#create it*
python3 -m venv venv

#activate it*
source venv/bin/activate

#check it*
where python
```
## Update Local Library
- Export a copy of your current item library
- Save it in this directory as 'currentcat.csv'

## Get Order Details
- Copy order details from the vendor website into 'data.txt' 

Example data.txt
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

```zsh
# Create a spreadsheet for the order
py minor-illusion.py

# Compare GTIN against existing library
py compare-gtin.py
```

- This will generate 'new_items.csv'
- Open 'new_items.csv' in your spreadsheet application of choice 

### Purchase Order Template
- Open 'library_template.xlsx' 
- The version included in this repo has some custom formatting to make your life easier

### Duplicate and Update Library Template 
Before you start working, duplicate the template and give it a useful name. Save to a shared drive and work from there.

*Adding New Item Data*
Now you are going to add the new items to the duplicate template you just created.  
- Open 'new_items.csv'
- Starting at row 2, copy the 'Item Name' Column from 'new_items.csv'
- Paste into your template using 'Paste and match style'
- Repeat for GTIN and Unit Cost 

Note: GTIN must be formatted as 'text'

*Pricing*
Once you have added Item Name, GTIN and Unit Costs, we need to add price
- Sort the template by ascending unit cost
- Use standard pricing practices 

*Finish the Template*
- Ensure all of the yellow columns are filled in: Reporting Category, Default Vendor Name, Tax
- Tax should be 'Y' in everything except for books
- Export the finished template to .xlsx file


## Import Template
- Import your freshly exported and updated template using
- DO NOT OVERWRIGHT THE ENTIRE EXISTING LIBRARY OR YOU WILL HAVE A BAD TIME 