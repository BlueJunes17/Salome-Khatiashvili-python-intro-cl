temp_tuple = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))

dailyaverage = ()
dailymax = ()
dailymin = ()

for i in temp_tuple:
    #საშუალო დღის
    dailyaverage += ( round(sum(i) / len(i),2), )
    #დღის მაქსიმუმი
    dailymax += ( max(i), )
    #დღის მინიმუმი
    dailymin += ( min(i), )

print ( f"დღის საშუალო ტემპერატურები: {dailyaverage}" )
print ( f"დღის მაქსიმალური ტემპერატურები: {dailymax}" )
print ( f"დღის მინიმალური ტემპერატურები: {dailymin}" )

#ვითვლით და ვპრინტავთ საშუალო დღეების საშუალოს
print(  f"საშუალო ტემპერატურა: {round(sum(dailyaverage) / len(dailyaverage),2)}" )