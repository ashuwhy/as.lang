a = " " 
b = " " 
c = " " 
d = " " 
e = " " 
f = " " 
g = " " 
h = " " 
i = " " 
game_running = 1 
cur_player = "2" 
no_tie = 1 
switch_player = 1 
while game_running
do {

output "
|  "+ a +"  |  "+ b +"  |  "+ c +"  |
|  "+ d +"  |  "+ e +"  |  "+ f +"  |
|  "+ g +"  |  "+ h +"  |  "+ i +"  |

" 

	if switch_player {
		if (cur_player == "1") {
			cur_player = "2"  
			turn = "x"
		}
		else {
			cur_player = "1"  
			turn = "o"
		}
	}
	else {
		nothing
	} 

	//inputs

	bad_move_msg = "
Illegal Move, type your move again!"

	choice = input "Player "+ cur_player + "(" + turn + ") Enter a choice (1-9): " 
	if choice == 1 {
		if g == " " {
			g = turn  switch_player = 1
		}
		else {
			output bad_move_msg  switch_player = 0
		}
	}
	else {
		if choice == 2 {
			if h == " " {
				h = turn  switch_player = 1
			}
			else {
				output bad_move_msg  switch_player = 0
			}
		}
		else {
			if choice == 3 {
				if i == " " {
					i = turn  switch_player = 1
				}
				else {
					output bad_move_msg  switch_player = 0
				}
			}
			else {
				if choice == 4 {
					if d == " " {
						d = turn  switch_player = 1
					}
					else {
						output bad_move_msg  switch_player = 0
					}
				}
				else {
					if choice == 5 {
						if e == " " {
							e = turn  switch_player = 1
						}
						else {
							output bad_move_msg  switch_player = 0
						}
					}
					else {
						if choice == 6 {
							if f == " " {
								f = turn  switch_player = 1
							}
							else {
								output bad_move_msg  switch_player = 0
							}
						}
						else {
							if choice == 7 {
								if a == " " {
									a = turn  switch_player = 1
								}
								else {
									output bad_move_msg  switch_player = 0
								}
							}
							else {
								if choice == 8 {
									if b == " " {
										b = turn  switch_player = 1
									}
									else {
										output bad_move_msg  switch_player = 0
									}
								}
								else {
									if choice == 9 {
										if c == " " {
											c = turn  switch_player = 1
										}
										else {
											output bad_move_msg  switch_player = 0
										}
									}
									else {
										switch_player = 0
									}
								}
							}
						}
					}
				}
			}
		}
	} 
	

	//game over logic
	if e != " " {
		if (a == e) and (e == i) {
			game_running = 0
		}
		else {	
			if (c == e) and (e == g) {
				game_running = 0
			}
			else {	
				if (d == e) and (e == f) {
					game_running = 0
				}
				else {	
					if (b == e) and (e == h) {
						game_running = 0
					}
					else {	
						nothing
					}
				}
			}
		}
	}
	else {
		nothing
	} 

	if a != " " {
		if (a == d) and (a == g) {
			game_running = 0
		}
		else {	
			if (a == b) and (a == c) {
				game_running = 0
			}
			else {	
				nothing
			}
		}
	}

	else {
		nothing
	} 

	if i != " " {
		if (i == h) and (i == g) {
			game_running = 0
		}
		else {	
			if (i == f) and (i == c) {
				game_running = 0
			}
			else {	
				nothing
			}
		}
	}
	else {
		nothing
	} 

	//tie logic
	if (a != " ") and (b != " ") and (c != " ") and (d != " ") and (e != " ") and (f != " ") and (g != " ") and (h != " ") and (i != " ") {
		game_running = 0  no_tie = 0
	}
	else {
		nothing
	}

}

output "
|  "+ a +"  |  "+ b +"  |  "+ c +"  |
|  "+ d +"  |  "+ e +"  |  "+ f +"  |
|  "+ g +"  |  "+ h +"  |  "+ i +"  |

" 

if no_tie {
	output "Game Over! Player "+ cur_player + "(" + turn + ") wins!" 
}
else {
	output "Game Over! Its a tie!" 
}
