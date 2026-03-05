import pandas as pd

df = pd.read_csv('data/messy_vocabulary_list.csv')

#Every EVEN row is main word line
main_wordline = df.iloc[::2].reset_index(drop=True)

#Every ODD row is a Hiragana Reading
hiragana = df.iloc[1::2].reset_index(drop=True)

#Combine them
main_wordline['Hiragana'] = hiragana['Vocabulary']

#Rename columns
final_df = main_wordline[['#', 'ごい', 'Hiragana', 'Vocabulary', 'Type', 'Meaning', 'Learning Status', 'Level']]
final_df.columns = ['#', 'Word', 'Hiragana', 'Romaji', 'Type', 'Meaning', 'Learning Status', 'Level']

#Save updates CSV file
final_df.to_csv('data/cleaned_vocabulary_list.csv', index=False)

print("Hiragana captured from the Vocabulary column Successfully")
print(final_df[['Word','Hiragana','Romaji']].head(5))