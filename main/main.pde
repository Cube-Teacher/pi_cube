import peasy.*;
import java.util.Scanner;
import java.io.IOException;

void settings() {
  System.setProperty("jogl.disable.openglcore", "true");
  size(500, 500, P3D);
}

float sideLength = 100;

RubikCube Cube;
debugTemplate Debug;
commandTemplate Command;
PeasyCam cam;

void setup(){
  noFill();
  Cube = new RubikCube(10,10);
  
  //  to init PeasyCam then we can easily to use mouse to rotate or move.
  cam = new PeasyCam(this,sideLength*3.0/2.0,sideLength*3.0/2,sideLength*3.0/2,1000);
  cam.setMinimumDistance(1000);
  cam.setMaximumDistance(2000);

  Command = new commandTemplate();
  Debug   = new debugTemplate();

  Cube.add_black();
}

void draw(){

  Cube.init();
  Command.read();
  background(255);
  // Debug.showcoordinate();
  // Debug.showcoordinateText();

  for(int i=0;i<3;i++){
    for(int j=0;j<3;j++){
      for(int k=0;k<3;k++){
        pushMatrix();

        if(Command.fileMutex == true){
          if(Command.processMutex==true){
            Command.enable(Command.command);
            Command.processMutex = false;
          }
        }

        // i==0 Green1 Blue3
        // i==1 Green2 Blue2
        // i==2 Green3 Blue1        
        if((i==0 && Cube.back1_clockwise)   || (i==1 && Cube.back2_clockwise)   || (i==2 && Cube.back3_clockwise) || 
           (i==0 && Cube.front3_clockwise)  || (i==1 && Cube.front2_clockwise)  || (i==2 && Cube.front1_clockwise) ){
          translate(150-(150*sqrt(2)*sin(radians(45-Cube.rotateAngle))),150-(150*sqrt(2)*cos(radians(45-Cube.rotateAngle))),0);
          rotateZ(radians(Cube.rotateAngle));
        }

        if((i==0 && Cube.back1_Counterclockwise)  || (i==1 && Cube.back2_Counterclockwise)  || (i==2 && Cube.back3_Counterclockwise) || 
           (i==0 && Cube.front3_Counterclockwise) || (i==1 && Cube.front2_Counterclockwise) || (i==2 && Cube.front1_Counterclockwise) ){
          translate(150-(150*sqrt(2)*cos(radians(-45+Cube.rotateAngle))),150+(150*sqrt(2)*sin(radians(-45+Cube.rotateAngle))),0);
          rotateZ(radians(-Cube.rotateAngle));
        }

        // j==0 White1 Yellow3
        // j==1 White2 Yellow2
        // j==2 White3 Yellow1
        if((j==0 && Cube.up1_clockwise)   || (j==1 && Cube.up2_clockwise)   || (j==2 && Cube.up3_clockwise) || 
           (j==0 && Cube.down3_clockwise) || (j==1 && Cube.down2_clockwise) || (j==2 && Cube.down1_clockwise)){
          translate(150-(150*sqrt(2)*cos(radians(45-Cube.rotateAngle))),0,150-(150*sqrt(2)*sin(radians(45-Cube.rotateAngle))));
          rotateY(radians(Cube.rotateAngle));
        }

        if((j==0 && Cube.up1_Counterclockwise)   || (j==1 && Cube.up2_Counterclockwise)   || (j==2 && Cube.up3_Counterclockwise) || 
           (j==0 && Cube.down3_Counterclockwise) || (j==1 && Cube.down2_Counterclockwise) || (j==2 && Cube.down1_Counterclockwise)){
          translate(150+(150*sqrt(2)*sin(radians(-45+Cube.rotateAngle))),0,150-(150*sqrt(2)*cos(radians(-45+Cube.rotateAngle))));
          rotateY(radians(-Cube.rotateAngle));
        }

        // k==0 Orange3 Red1
        // k==1 Orange2 Red2
        // k==2 Orange1 Red3
        if((k==0 && Cube.right3_clockwise)  || (k==1 && Cube.right2_clockwise) || (k==2 && Cube.right1_clockwise) ||
           (k==0 && Cube.left1_clockwise)   || (k==1 && Cube.left2_clockwise)  || (k==2 && Cube.left3_clockwise)){
          translate(0,150-(150*sqrt(2)*sin(radians(45-Cube.rotateAngle))),150-(150*sqrt(2)*cos(radians(45-Cube.rotateAngle))));
          rotateX(radians(Cube.rotateAngle));
        }

        if((k==0 && Cube.right3_Counterclockwise) || (k==1 && Cube.right2_Counterclockwise) || (k==2 && Cube.right1_Counterclockwise) ||
           (k==0 && Cube.left1_Counterclockwise)  || (k==1 && Cube.left2_Counterclockwise)  || (k==2 && Cube.left3_Counterclockwise)){
          translate(0,150-(150*sqrt(2)*cos(radians(-45+Cube.rotateAngle))),150+(150*sqrt(2)*sin(radians(-45+Cube.rotateAngle))));
          rotateX(radians(-Cube.rotateAngle));
        }
        
        // translate(sideLength*-1+k*sideLength, sideLength*-1+j*sideLength, sideLength*-1+i*sideLength);
        translate(sideLength/2+k*sideLength, sideLength/2+j*sideLength, sideLength/2+i*sideLength);
        Cube.cubebox[k][j][i].creatBox();
        popMatrix();
      }
    }
  }

  if(Command.processMutex == false){
    Cube.updateHandler();
  }
}


