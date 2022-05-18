import commands2
from wpimath.controller import PIDController
from constants import movement_K_p, movement_K_I, movement_K_D
from subsytems.drivetrain import Drivetrain

class DriveStraight(commands2.PIDCommand):
    # /**
    # * Creates a new DriveStraight.
    # */
    def __init__(self, distSetPt: float, drivetrain: Drivetrain):
        super().__init__(
            PIDController(movement_K_p, movement_K_I,
                          movement_K_D),

            drivetrain.m_left_encoder.getPosition,

            distSetPt,

            drivetrain.driveStraight,
            [drivetrain])

    def isFinished(self):
        return self.getController().atSetpoint();
