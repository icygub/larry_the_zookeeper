import time, sys

def format_quote(quote): #trying to figure out how i would use this
    return quote[0] + ': ' + quote[1]
        
def store_file(filename):
    file = open(filename) #directory
    file_content = file.readlines()
    dialog = []
    
    for line in file_content:
        try:
            ind = line.index(':')
            dialog.append( (line[0:ind].strip(), line[ind+1:].strip()) )
        except:
            dialog.append( line.strip() )
    return dialog

def print_delayed_text(text, delay):
    for letter in text:
        print(letter,end='')
        sys.stdout.flush()
        time.sleep(delay)

def print_quote(quote):
    if type(quote) == tuple:
        print_delayed_text(quote[0] + ': ', .05)
        print_delayed_text(quote[1] + '\n', .2)
    else:
        print_delayed_text(quote, .05)
        print_delayed_text('\n', .2)

def main():
    if len(sys.argv) != 2:
        print("You must provide a filename my friend.")
        return
    
    dialog = store_file(sys.argv[1])
    
    for quote in dialog:
        print_quote(quote)
    
if __name__ == '__main__':
    main()
