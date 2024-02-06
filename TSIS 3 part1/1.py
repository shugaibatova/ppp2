# A recipe you are reading states how many grams you need for the ingredient.
#  Unfortunately, your store only sells items in ounces.
#  Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def ounces(grams):
    grams*=28.3495231
    print (grams ,"ounces")
    
ounces(344)
ounces(5)