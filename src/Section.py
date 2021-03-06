# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):
        self.vertices = [ 
                [0, 0, 0 ], #0
                [0, 0, self.parameters['height']], #1
                [self.parameters['width'], 0, self.parameters['height']], #2
                [self.parameters['width'], 0, 0],      #3
				[0,self.parameters['thickness'],0],    #4
                [0,self.parameters['thickness'],self.parameters['height']], #5
                [self.parameters['width'],self.parameters['thickness'],self.parameters['height']],  #6
                [self.parameters['width'],self.parameters['thickness'],0] #7
                ]
        self.faces = [
                [0,3,2,1],
                [4,7,6,5],
                [3,7,6,2],
                [0,4,5,1],
                [0,3,7,4],
                [1,2,6,5],
                
                ]  

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        if self.getParameter('position')[0] + self.getParameter('width') < x.getParameter('position')[0] + x.getParameter('width'):
            #si la position (en x) + la longueur du mur < position + longueur de l'ouverture : ce n'est pas possible 
            return False
        elif x.getParameter('position')[0] + x.getParameter('width') < self.getParameter('position')[0]:
            #si la position (en x)  + la longueur de la fen??tre < la position de d??part du mur : ce n'est pas possible non plus (on ne peut pas faire d'ouverture dans le vide)
            return False
        elif self.getParameter('position')[2] + self.getParameter('height') < x.getParameter('position')[2] + x.getParameter('height'):
            #si la position (en z) + la hauteur du mur < position + hauteur de l'ouverture : ce n'est pas possible 
            return False
        elif x.getParameter('position')[2] + x.getParameter('height') < self.getParameter('position')[2]:
            #si la position (en z)  + la hauteur de la fen??tre < la position de d??part du mur : ce n'est pas possible non plus (on ne peut pas faire d'ouverture dans le vide)
            return False
        elif self.getParameter('thickness') != x.getParameter('thickness'):
            #si l'??paisseur du mur est diff??rente de celle de l'ouverture : on ne peut pas la faire 
            return False
        else :
            return True    
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compl??ter en rempla??ant pass par votre code
        pass              
        
    # Draws the edges
    def drawEdges(self):
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glRotate(self.parameters['orientation'],0,0,1)
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)    
        for x in self.faces:
            gl.glBegin(gl.GL_QUADS)
            gl.glColor3fv([0, 0, 0])
            gl.glVertex3fv(self.vertices[x[0]]) 
            gl.glVertex3fv(self.vertices[x[1]]) 
            gl.glVertex3fv(self.vertices[x[2]]) 
            gl.glVertex3fv(self.vertices[x[3]]) 
            gl.glEnd()
        gl.glPopMatrix() #permet de restaurer les coordonn??es du syst??me pr??c??dent         
                    
    # Draws the faces
    def draw(self):
        if self.parameters['edges']: #si le param??tre "edges" prend la valeur "true" alors le dessin des faces peut avoir lieu
            self.drawEdges()
            
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glRotate(self.parameters['orientation'],0,0,1)
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_FILL)
        for x in self.faces: 
            gl.glBegin(gl.GL_QUADS) 
            gl.glColor3fv([0.5, 0.5, 0.5]) 
            gl.glVertex3fv(self.vertices[x[0]])
            gl.glVertex3fv(self.vertices[x[1]])
            gl.glVertex3fv(self.vertices[x[2]])
            gl.glVertex3fv(self.vertices[x[3]])
            gl.glEnd()
        gl.glPopMatrix() 
  