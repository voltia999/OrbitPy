import numpy as np
from planets import Planets
from constants import MU

class Orbits:
    def __init__(self,planets: Planets):
        
        self.planets = planets
        self.RB = self.planets.orbital_radiusB
        self.TB = self.planets.orbital_periodB
        self.mu_B = self.planets.muB
        self.omega_B = 2 * np.pi / self.TB  # average angular velocity
        self.vorb_B = self.omega_B * self.RB

    def orbitB (self, t, Y, phi):
        """
        Calculate the position and velocity of the planet B in its circular orbit.
    
        Parameters:
        - t: time array
        - Y: state vector of the vehicle [x, y, z, vx, vy, vz]
        - phi: initial phase of the planet B's orbit

        Returns:
        - FF: vector [x, y, z, vx, vy, vz] of the planet B at the instant t
        """
        FF = np.zeros_like(Y)
        
        theta = self.omega_B * t - phi 

        #Orbit equations of the planet B    
        FF[0] = self.RB * np.cos(theta)
        FF[1] = self.RB * np.sin(theta) 
        FF[2] = 0
        FF[3] = self.vorb_B * (-np.sin(theta))
        FF[4] = self.vorb_B * np.cos(theta)
        FF[5] = 0
        return FF

    def F(self, t, Y, phi):
        """Compute the time derivative of the spacecraft state vector based on the
        gravitational influence of the Sun and planet B.

        This function represents the system of differential equations that govern
        the spacecraft's motion in a simplified three-body problem.

        Parameters:
        - t (float): Current time.
        - Y (ndarray): State vector of the spacecraft [x, y, z, vx, vy, vz].
        - phi (float): Initial phase angle of planet B's orbit.

        Returns:
        - ndarray: Time derivative of the state vector [vx, vy, vz, ax, ay, az].
        """
        
        FF = np.zeros_like(Y) 

        R = self.orbitaB(t,Y, phi)
        r = (Y[0]**2 + Y[1]**2 + Y[2]**2)** (3/2)
        radius = np.sqrt((Y[0] -R [0])**2 + (Y[1] -R [1])**2 + (Y[2] -R [2])**2)

        radius = radius*radius*radius
        RADIO = self.RB*self.RB*self.RB 

        #Ecuaciones dinámicas para el vehículo espacial
        FF[0] = Y[3]
        FF[1] = Y[4]
        FF[2] = Y[5]   
        FF[3] = -MU * Y[0] / (r) - self.mu_B * ((Y[0] - R[0])/radius + R[0]/RADIO) 
        FF[4] = -MU * Y[1] / (r) - self.mu_B * ((Y[1] - R[1])/radius + R[1]/RADIO)
        FF[5] = -MU * Y[2] / (r) - self.mu_B * ((Y[2] - R[2])/radius + R[2]/RADIO)
        return FF

