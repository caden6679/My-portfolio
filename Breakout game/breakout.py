"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is a Breakout game where the player controls a paddle
to bounce a ball and break bricks. The goal is to clear all
the bricks without losing all lives. The player has a limited
number of lives, and if the ball hits the bottom of the window,
they lose one life. If all bricks are cleared, the player wins.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    num_lives = 0
    while True:
        if num_lives < NUM_LIVES:
            if graphics.remaining_bricks == 0:
                # All bricks are cleared, the game is over.
                graphics.game_win()
                graphics.reset_ball_position()
            else:
                onmouseclicked(graphics.start)
                if graphics.game_start:
                    graphics.ball.move(graphics.ball_vx, graphics.ball_vy)
                    print(graphics.ball_vx)
                    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                        graphics.ball_vx = -graphics.ball_vx
                    if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
                        graphics.game_start = False
                        num_lives = num_lives+1
                        graphics.reset_ball_position()
                    graphics.handle_collision()
                    pause(FRAME_RATE)
        else:
            graphics.game_loss()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
