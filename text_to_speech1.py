from text_to_speech import save
import webbrowser

text = input("enter text to search : ")
webbrowser.open(f"https://www.google.com/search?q={text.replace(' ', '+')}")


lang = 'en'
output_file = input("enter filename : ")
output_file+=".mp3"

save(text,lang,file=output_file)
print("audio created on :",output_file)