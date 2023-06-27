import turtle


class PongGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.turtle_pointer = turtle.Turtle()
        self.player_one = turtle.Turtle()
        self.player_two = turtle.Turtle()
        self.screen.setup(1050, 650)

        self.ball = turtle.Turtle()
        self.ball_dx = 7
        self.ball_dy = 5

        self.player_one_score = 0
        self.player_two_score = 0
        self.score = turtle.Turtle()

        self.display_gadgets()
        self.key_listen()
        self.game_play()

    @staticmethod
    def mainloop():
        turtle.done()

    def player_one_creation(self):
        self.player_one.speed(0)
        self.player_one.shape('square')
        self.player_one.color('black')
        self.player_one.shapesize(stretch_wid=6, stretch_len=2)
        self.player_one.penup()
        self.player_one.goto(-400, 0)

    def player_two_creation(self):
        self.player_two.speed(0)
        self.player_two.shape('square')
        self.player_two.color('black')
        self.player_two.shapesize(stretch_wid=6, stretch_len=2)
        self.player_two.penup()
        self.player_two.goto(400, 0)

    def ball_creation(self):
        self.ball.speed(0)
        self.ball.shape('circle')
        self.ball.color('blue')
        self.ball.penup()
        self.ball.goto(0, 0)

    def display_score(self):
        self.score.speed(0)
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0, 260)
        self.score.write('Player 1: 0 Player 2: 0', align='center', font=('Courier', 20, 'bold'))

    def move_player_one_up(self):
        y = self.player_one.ycor()
        y += 15
        self.player_one.sety(y)

    def move_player_one_down(self):
        y = self.player_one.ycor()
        y -= 15
        self.player_one.sety(y)

    def move_player_two_up(self):
        y = self.player_two.ycor()
        y += 15
        self.player_two.sety(y)

    def move_player_two_down(self):
        y = self.player_two.ycor()
        y -= 15
        self.player_two.sety(y)

    def key_listen(self):
        self.screen.onkeypress(self.move_player_one_up, 'w')
        self.screen.onkeypress(self.move_player_one_down, 's')
        self.screen.onkeypress(self.move_player_two_up, 'Up')
        self.screen.onkeypress(self.move_player_two_down, 'Down')
        self.screen.listen()

    def display_gadgets(self):
        self.player_one_creation()
        self.player_two_creation()
        self.ball_creation()
        self.display_score()

    def game_play(self):
        while True:
            self.screen.update()

            self.ball.setx(self.ball.xcor() + self.ball_dx)
            self.ball.sety(self.ball.ycor() + self.ball_dy)

            if self.ball.ycor() < -300 or self.ball.ycor() > 300:
                self.ball_dy *= -1

            if self.ball.xcor() > 500 or self.ball.xcor() < -500:
                if self.ball.xcor() < -500:
                    self.player_two_score += 1
                else:
                    self.player_one_score += 1

                self.ball.goto(0, 0)
                self.ball_dx *= -1
                self.ball_dy *= -1

                self.score.clear()
                self.score.write(f'Player 1 {self.player_one_score} Player 2: {self.player_two_score}', align='center',
                                 font=('Courier', 20, 'bold'))

            if -360 > self.ball.xcor() > -370 and self.player_one.ycor() + 50 > self.ball.ycor() >\
                    self.player_one.ycor() - 50:
                self.ball.setx(-360)
                self.ball_dx *= -1

            if 370 > self.ball.xcor() > 360 and self.player_two.ycor() + 50 > self.ball.ycor() >\
                    self.player_two.ycor() - 50:
                self.ball.setx(360)
                self.ball_dx *= -1


PongGame().mainloop()
