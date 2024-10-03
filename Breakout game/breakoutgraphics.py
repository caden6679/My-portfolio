"""
File: breakout.py
Name: Alastair
--------------------------
This file demonstrates how to use the command line
to run different functions of the Breakout game.
We will be using the 'sys' module to handle this process.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=self.window_width/2-paddle_width/2, y=self.window_height - paddle_offset)
        # Center a filled ball in the graphical window
        self.ball_start_x = self.window_width / 2-BALL_RADIUS/2
        self.ball_start_y = self.window_height/2-BALL_RADIUS/2
        self.ball = GOval(BALL_RADIUS, BALL_RADIUS, x=self.ball_start_x, y=self.ball_start_y)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.ball_vx = self.get_ball_vx()
        self.ball_vy = self.get_ball_vy()
        # Initialize our mouse listeners
        self.game_start = False
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start)

        # Judge win or lose
        self.remaining_bricks = 0  # Set the counter to zero
        self.loss = GLabel('You lose')
        self.loss.font = '-50'

        self.win = GLabel('You win')
        self.win.font = '-50'

        # Draw bricks
        self.bricks = []
        self.create_bricks(brick_rows, brick_cols, BRICK_OFFSET)

    def create_bricks(self, brick_rows, brick_cols, BRICK_OFFSET):
        """
        Creates a grid of bricks, sets their color based on the row number, and adds them to the window and brick list.
        """
        colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange']
        for row in range(brick_rows):
            for col in range(brick_cols):
                x = col * (BRICK_WIDTH + BRICK_SPACING)
                y = row * (BRICK_HEIGHT + BRICK_SPACING) + BRICK_OFFSET

                # Use the row number to determine the color by taking the remainder
                brick_color = colors[row // 2 % len(colors)]

                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.filled = True
                brick.fill_color = brick_color
                self.window.add(brick, x, y)
                self.bricks.append(brick)  # Add each created brick to the list
                self.remaining_bricks += 1  # Increase the counter by 1"

    def move_paddle(self, event):
        """
        Moves the paddle based on the mouse position while keeping it within the screen boundaries.
        """
        # Find the center of the paddle
        paddle_center = event.x - self.paddle.width/2
        # Keep the paddle within the screen
        if 0 <= paddle_center <= self.window.width - self.paddle.width:
            self.paddle.x = paddle_center

    def start(self, event):
        """
        Starts the game and prints the vertical speed of the ball.
        """
        self.game_start = True
        print(self.__dy)

    def get_ball_vx(self):
        """
        Generates a random horizontal speed for the ball, which could be positive or negative.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() < 0.5:
            self.__dx *= -1
        return self.__dx

    def get_ball_vy(self):
        """
        Returns the initial vertical speed of the ball.
        """
        self.__dy = INITIAL_Y_SPEED
        return self.__dy

    def get_ball_coordinates(self):
        """
        Retrieves the coordinates of the four corners of the ball: top-left, top-right, bottom-left, and bottom-right.
        """
        # Top-left corner
        top_left = (self.ball.x, self.ball.y)

        # Top-right corner
        top_right = (self.ball.x + self.ball.width, self.ball.y)

        # Bottom-left corner
        bottom_left = (self.ball.x, self.ball.y + self.ball.height)

        # Bottom-right corner
        bottom_right = (self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        return top_left, top_right, bottom_left, bottom_right

    def handle_collision(self):
        """
        Detects collisions between the ball and the paddle or bricks.
        Adjusts ball direction and removes bricks when hit.
        """
        ball_coordinates = self.get_ball_coordinates()
        for coordinate in ball_coordinates:
            obj = self.window.get_object_at(coordinate[0], coordinate[1])
            if obj is not None:
                # If the ball hits the paddle
                if obj == self.paddle:
                    self.ball_vy = -self.ball_vy
                    break
                # If the ball hits a brick
                if obj in self.bricks:
                    self.window.remove(obj)
                    self.ball_vy = -self.ball_vy
                    self.remaining_bricks -= 1  # Reduce the brick count by 1

                    break  # End the loop to avoid multiple collision checks

    def reset_ball_position(self):
        """
        Resets the ball's position to the starting point and assigns new speed values.
        """
        self.ball.x = self.ball_start_x
        self.ball.y = self.ball_start_y
        self.ball_vx = self.get_ball_vx()
        self.ball_vy = self.get_ball_vy()

    def game_loss(self):
        """
        Displays the "You Lose" message on the screen.
        """
        self.window.add(self.loss, self.window_width / 2-self.loss.width/2, self.window_height / 2-self.loss.height/2)

    def game_win(self):
        """
        Displays the "You Win" message on the screen and stops the game.
        """
        self.window.add(self.win, self.window_width / 2 - self.win.width / 2,
                        self.window_height / 2 - self.win.height / 2)
        self.game_start = False  # End the game
