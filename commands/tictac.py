import numpy as np

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


a = np.array(board)
for row in board:
    for number in row:
        if number == 5:
            b = np.where(a==number)
            x = b[0][0]
            y = b[1][0]
            board[x][y] = "X"

for row in board:
    print(row)

#                 person = message.author
#                 corners = [1,3,7,9]
#                 rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#                 used = []
#                 def get_new(rows):
#                     return f"""``` {rows[0][0]}| {rows[0][1]}| {rows[0][2]}
# --+--+--
#  {rows[1][0]}| {rows[1][1]}| {rows[1][2]}
# --+--+--
#  {rows[2][0]}| {rows[2][1]}| {rows[2][2]} ```"""

#                 def place_symbol(rows, field, used):
#                     global iteration
#                     for row in rows:
#                         for number in row:
#                             if number == field:
#                                 b = np.where(a==field)
#                                 x = b[0][0]
#                                 y = b[1][0]
#                                 if iteration % 2 == 0:
#                                     rows[x][y] = "O"
#                                 else:
#                                     rows[x][y] = "X"
#                                 iteration += 1
#                                 used.append(number)
#                     rows = get_new(rows)
#                     return rows
				
#                 def get_option(num):
#                     if num % 2 == 0:
#                         option = "side"
#                     elif num == 5:
#                         option = "middle"
#                     else:
#                         option = "corner"
#                     return option

#                 def get_across_corners(rows,num):
#                     if num <= 3:
#                         x = 2
#                         if np.where(a==num)[1][0] == 1:
#                             y = 2
#                         else:
#                             y = 0
#                     else:
#                         x = 0
#                         if np.where(a==num)[1][0] == 7:
#                             y = 2
#                         else:
#                             y = 0
#                     return rows[x][y]

#                 def check_availabile(used, num):
#                     availabile = True
#                     for number in used:
#                         if num == number:
#                             availabile = False
#                     return availabile


#                 #make it for two players!!!
#                 a = np.array(rows)
#                 done = False
#                 starting_point = random.randint(1,9)
#                 await message.channel.send(place_symbol(rows, starting_point, used=used))
#                 while True:
#                     message = await client.wait_for("message")
#                     if message.author == person:
#                         field = message.content
#                         if isint(field):
#                             field = int(field)
#                             for num in used:
#                                 if num == field:
#                                     await message.channel.send("This place is already taken!")
#                                     break
							
#                             place_symbol(rows, field, used=used)
#                             option = get_option(field)
#                             if option == "corner":
#                                 pass
#                             elif option == "side":
#                                 if done == False:
#                                     place_symbol(rows, field=5, used=used)
#                                     done = True
#                             global iteration
#                             if iteration == 4:
#                                 across = get_across_corners(rows=rows, num=starting_point)
#                                 if isint(across) == True and option == "side":
#                                     await message.channel.send("ur stoopid")
#                                     place_symbol(rows, field=int(across), used=used)
#                                 else:
#                                     corner_options = []
#                                     availability = []
#                                     for num in corners:
#                                         if check_availabile(used, num):
#                                             corner_options.append(num)
#                                     for option in corner_options:
#                                         if option == 1 or option == 3:
#                                             num = 2
#                                         else:
#                                             num = 8
#                                         availability.append(check_availabile(used, num))
#                                     if availability[0] == True and availability[1] == True:
#                                         pass
#                                     else:
#                                         pass

#                             elif iteration > 4:
#                                 pass
								

							

								

#                             await message.channel.send(get_new(rows))
#                         elif field.lower() == "quit":
#                             iteration = 0
#                             break
#                         else:
#                             await message.channel.send("A number please!")