import commands2
import ctre
from wpilib.drive import DifferentialDrive
from wpilib import SpeedControllerGroup


class Drivetrain(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.gyro = ctre.PigeonIMU(10)
        self.gyro.setYaw(0, 0)

        self.m_left = ctre.WPI_TalonSRX(0)
        self.m_left_2 = ctre.WPI_VictorSPX(1)
        self.m_left_3 = ctre.WPI_VictorSPX(2)
        self.m_right = ctre.WPI_TalonSRX(3)
        self.m_right_2 = ctre.WPI_VictorSPX(4)
        self.m_right_3 = ctre.WPI_VictorSPX(5)

        self.m_left_2.follow(self.m_left)
        self.m_left_3.follow(self.m_left)

        self.m_right_2.follow(self.m_right)
        self.m_right_3.follow(self.m_right)

        self.leftMotors = SpeedControllerGroup(ctre.WPI_TalonSRX(0), ctre.WPI_VictorSPX(1), ctre.WPI_VictorSPX(2))
        self.rightMotors = SpeedControllerGroup(ctre.WPI_TalonSRX(3), ctre.WPI_VictorSPX(4), ctre.WPI_VictorSPX(5))

        self.m_right_encoder = ctre.CANCoder(9)
        self.m_left_encoder = ctre.CANCoder(11)

        self.drive = DifferentialDrive(self.leftMotors, self.rightMotors)

    def set(self, left: float, right: float):
        """ a tank drive for the robot."""
        self.drive.tankDrive(left, -right)
        # self.m_left.set(ctre.ControlMode.PercentOutput, left)
        # self.m_right.set(ctre.ControlMode.PercentOutput, -right)

    def arcadeDrive(self, fwd, rot):
        """Drive the robot with standard arcade controls."""
        self.drive.arcadeDrive(fwd, rot)
        # self.set(fwd-rot, fwd+rot)

    def periodic(self):
        pass

    def driveStraight(self, fwd):
        self.arcadeDrive(fwd, 0)
