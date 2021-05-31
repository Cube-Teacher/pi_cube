
/*
boxTemplate:
Box is a little cube of out RubikCube. 
Hence, we will use 27 cubes to constuct RubikCube.
Since there are 6 colors on RubikCube. We also need color attribute of little cube.
*/
class boxTemplate{
  String  upFace         ;
  String  downFace       ;
  String  leftFace       ;
  String  rightFace      ;
  String  frontFace      ;
  String  backFace       ;
  float   len            ;
  float   lineThickness  ;

  // constructor
  boxTemplate(){
    upFace          = "WHITE";
    downFace        = "YELLOW";
    rightFace       = "ORANGE";
    leftFace        = "RED";
    backFace        = "GREEN";
    frontFace       = "BLUE";
    len             = sideLength/2;
    lineThickness   = 10;
  }

  void creatBox(){
    beginShape(QUADS);

    strokeWeight(this.lineThickness);
    len = this.len;

    // TOP
    fill(find_color(this.upFace));
    vertex(-len, -len, -len);
    vertex( len, -len, -len);
    vertex( len, -len,  len);
    vertex(-len, -len,  len);
    
    // DOWN
    fill(find_color(this.downFace));
    vertex(-len,  len, -len);
    vertex( len,  len, -len);
    vertex( len,  len,  len);
    vertex(-len,  len,  len);

    // 
    fill(find_color(this.rightFace));
    vertex( len, -len, -len);
    vertex( len, -len,  len);
    vertex( len,  len,  len);
    vertex( len,  len, -len);
    
    // 
    fill(find_color(this.leftFace));
    vertex(-len, -len, -len);
    vertex(-len, -len,  len);
    vertex(-len,  len,  len);
    vertex(-len,  len, -len);

    // 
    fill(find_color(this.backFace));
    vertex( len, -len, -len);
    vertex(-len, -len, -len);
    vertex(-len,  len, -len);
    vertex( len,  len, -len);
    
    // 
    fill(find_color(this.frontFace));
    vertex( len, -len,  len);
    vertex(-len, -len,  len);
    vertex(-len,  len,  len);
    vertex( len,  len,  len);

    strokeWeight(1);
    endShape();
  }
}

class RubikCube {
  float cubeLinethickness           ;
  float sideLinethickness           ;
  boxTemplate[][][] cubebox         ;
  boxTemplate[][][] prebox          ;

  /*
    Interface for outside command to control RubikCube rotating.
  */
  boolean right1_Counterclockwise   ;
  boolean right2_Counterclockwise   ;
  boolean right3_Counterclockwise   ;
  boolean left1_Counterclockwise    ;
  boolean left2_Counterclockwise    ;
  boolean left3_Counterclockwise    ;

  boolean back1_Counterclockwise    ;
  boolean back2_Counterclockwise    ;
  boolean back3_Counterclockwise    ;
  boolean front1_Counterclockwise   ;
  boolean front2_Counterclockwise   ;  
  boolean front3_Counterclockwise   ;

  boolean up1_Counterclockwise      ;
  boolean up2_Counterclockwise      ;
  boolean up3_Counterclockwise      ;
  boolean down1_Counterclockwise    ;
  boolean down2_Counterclockwise    ;
  boolean down3_Counterclockwise    ;

  boolean right1_clockwise          ;
  boolean right2_clockwise          ;
  boolean right3_clockwise          ;
  boolean left1_clockwise           ;
  boolean left2_clockwise           ;
  boolean left3_clockwise           ;

  boolean back1_clockwise           ;
  boolean back2_clockwise           ;
  boolean back3_clockwise           ;
  boolean front1_clockwise          ;
  boolean front2_clockwise          ;        
  boolean front3_clockwise          ;

  boolean up1_clockwise             ;
  boolean up2_clockwise             ;
  boolean up3_clockwise             ;
  boolean down1_clockwise           ;
  boolean down2_clockwise           ;
  boolean down3_clockwise           ;

  boolean up_right;
  boolean up_left;
  boolean up_back;
  boolean up_front;
  boolean up_fix_right;
  boolean up_fix_left;

  float rotateAngle;
  float rotateSpeed;

  RubikCube(float cubeLinethickness, float sideLinethickness){
    this.cubeLinethickness = cubeLinethickness;
    this.sideLinethickness = sideLinethickness;
    this.cubebox = new boxTemplate[3][3][3];
    for(int i=0;i<3;i++){
      for(int j=0;j<3;j++){
        for(int k=0;k<3;k++){
          cubebox[i][j][k] = new boxTemplate();
        }
      }
    }
    
    this.prebox = new boxTemplate[3][3][3];
    for(int i=0;i<3;i++){
      for(int j=0;j<3;j++){
        for(int k=0;k<3;k++){
          prebox[i][j][k] = new boxTemplate();
        }
      }
    }

    this.right1_Counterclockwise    = false ;
    this.right2_Counterclockwise    = false ;
    this.right3_Counterclockwise    = false ;
    this.left1_Counterclockwise     = false ;
    this.left2_Counterclockwise     = false ;
    this.left3_Counterclockwise     = false ;

    this.back1_Counterclockwise     = false ;
    this.back2_Counterclockwise     = false ;
    this.back3_Counterclockwise     = false ;
    this.front1_Counterclockwise    = false ;
    this.front2_Counterclockwise    = false ;  
    this.front3_Counterclockwise    = false ;

    this.up1_Counterclockwise       = false ;
    this.up2_Counterclockwise       = false ;
    this.up3_Counterclockwise       = false ;
    this.down1_Counterclockwise     = false ;
    this.down2_Counterclockwise     = false ;
    this.down3_Counterclockwise     = false ;

    this.right1_clockwise           = false ;
    this.right2_clockwise           = false ;
    this.right3_clockwise           = false ;
    this.left1_clockwise            = false ;
    this.left2_clockwise            = false ;
    this.left3_clockwise            = false ;

    this.back1_clockwise            = false ;
    this.back2_clockwise            = false ;
    this.back3_clockwise            = false ;
    this.front1_clockwise           = false ;
    this.front2_clockwise           = false ;  
    this.front3_clockwise           = false ;

    this.up1_clockwise              = false ;
    this.up2_clockwise              = false ;
    this.up3_clockwise              = false ;
    this.down1_clockwise            = false ;
    this.down2_clockwise            = false ;
    this.down3_clockwise            = false ;

    this.up_right                   = false ;
    this.up_left                    = false ;
    this.up_back                    = false ;
    this.up_front                   = false ;
    this.up_fix_right               = false ;
    this.up_fix_left                = false ;

    this.rotateAngle = 0.0;
    this.rotateSpeed = 1.0;
  }

  String switch_init(String init){
    if(init.equals("WHITE")){
      return "WHITE";
    } else if(init.equals("YELLOW")){
      return "YELLOW";
    } else if(init.equals("RED")){
      return "RED";
    } else if(init.equals("GREEN")){
      return "GREEN";
    } else if(init.equals("BLUE")){
      return "BLUE";
    } else if(init.equals("ORANGE")){
      return "ORANGE";
    }
    return "";
  }

  void init(){
    String[] tmp_init = loadStrings("../sol/init.txt");
		if(tmp_init.length==54){
      for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
          Cube.cubebox[j][0][i].upFace    = switch_init(tmp_init[i*3+j]);
        }
      }
      for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
          Cube.cubebox[j][i][2].frontFace = switch_init(tmp_init[i*3+j+9]);
        }
      }
      for(int i=0;i<3;i++){
        for(int j=2;j>=0;j--){
          Cube.cubebox[j][i][0].backFace  = switch_init(tmp_init[i*3+2-j+18]);
        }
      }
      for(int i=0;i<3;i++){
        for(int j=2;j>=0;j--){
          Cube.cubebox[2][i][j].rightFace = switch_init(tmp_init[i*3+2-j+27]);
        }
      }
      for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
          Cube.cubebox[0][i][j].leftFace  = switch_init(tmp_init[i*3+j+36]);
        }
      }
      for(int i=2;i>=0;i--){
        for(int j=0;j<3;j++){
          Cube.cubebox[j][2][i].downFace  = switch_init(tmp_init[(2-i)*3+j+45]);
        }
      }
      PrintWriter outputfile_tmp;
      outputfile_tmp = createWriter("../sol/init.txt");
      outputfile_tmp.print("");
      outputfile_tmp.flush();
      outputfile_tmp.close();
		}
  }

  void add_black(){
    for(int i=0;i<3;i++){
      for(int k=0;k<2;k++){
        for(int j=0;j<3;j++){
          this.cubebox[j][i][k].frontFace = "BLACK";
        }
      }
      for(int k=1;k<3;k++){
        for(int j=0;j<3;j++){
          this.cubebox[j][i][k].backFace = "BLACK";
        }
      }
      for(int k=0;k<2;k++){
        for(int j=0;j<3;j++){
          this.cubebox[k][i][j].rightFace = "BLACK";
        }
      }
      for(int k=1;k<3;k++){
        for(int j=0;j<3;j++){
          this.cubebox[k][i][j].leftFace = "BLACK";
        }
      }
      if(i==0 || i==1){
        for(int k=0;k<3;k++){
          for(int j=0;j<3;j++){
            this.cubebox[k][i][j].downFace = "BLACK";
          }
        }
      }
      if(i==1 || i==2){
        for(int k=0;k<3;k++){
          for(int j=0;j<3;j++){
            this.cubebox[k][i][j].upFace = "BLACK";
          }
        }
      }
    }
  }
  
  void createSurface(float len){
    CubeSurface(this.cubeLinethickness, len);
  }

  void createSideline(){
    CubeLine(this.sideLinethickness);
  }

  void updateHandler(){
    Cube.rotateAngle += Cube.rotateSpeed;
    if(Cube.rotateAngle>90){
      Cube.update();
      Cube.rotateAngle = 0.0;
      Command.processMutex = true;
      Command.clear();
    }
  }

  void update(){
    if(Command.command.equals("up_right")){
			Cube.Updatefront1();
      Cube.Updatefront2();
      Cube.Updatefront3();
		} else if(Command.command.equals("up_left")){
      Cube.Update_Counterclockwise_front1();
      Cube.Update_Counterclockwise_front2();
      Cube.Update_Counterclockwise_front3();
		} else if(Command.command.equals("up_back")){
      Cube.Updateleft1();
      Cube.Updateleft2();
      Cube.Updateleft3();
		} else if(Command.command.equals("up_front")){
      Cube.Update_Counterclockwise_left1();
      Cube.Update_Counterclockwise_left2();
      Cube.Update_Counterclockwise_left3();
		} else if(Command.command.equals("up_fix_right")){
      Cube.Update_Counterclockwise_up1();
      Cube.Update_Counterclockwise_up2();
      Cube.Update_Counterclockwise_up3();
		} else if(Command.command.equals("up_fix_left")){
      Cube.Updateup1();
      Cube.Updateup2();
      Cube.Updateup3();
		} else {
      if(Command.command.equals("back1_clockwise")){
        Cube.Updateback1();
      } else if(Command.command.equals("back2_clockwise")){
        Cube.Updateback2();
      } else if(Command.command.equals("back3_clockwise")){
        Cube.Updateback3();
      } else if(Command.command.equals("left1_clockwise")){
        Cube.Updateleft1();
      } else if(Command.command.equals("left2_clockwise")){
        Cube.Updateleft2();
      } else if(Command.command.equals("left3_clockwise")){
        Cube.Updateleft3();
      } else if(Command.command.equals("down1_clockwise")){
        Cube.Updatedown1();
      } else if(Command.command.equals("down2_clockwise")){
        Cube.Updatedown2();
      } else if(Command.command.equals("down3_clockwise")){
        Cube.Updatedown3();
      } else if(Command.command.equals("front1_clockwise")){
        Cube.Updatefront1();
      } else if(Command.command.equals("front2_clockwise")){
        Cube.Updatefront2();
      } else if(Command.command.equals("front3_clockwise")){
        Cube.Updatefront3();
      } else if(Command.command.equals("right1_clockwise")){
        Cube.Updateright1();
      } else if(Command.command.equals("right2_clockwise")){
        Cube.Updateright2();
      } else if(Command.command.equals("right3_clockwise")){
        Cube.Updateright3();
      } else if(Command.command.equals("up1_clockwise")){
        Cube.Updateup1();
      } else if(Command.command.equals("up2_clockwise")){
        Cube.Updateup2();
      } else if(Command.command.equals("up3_clockwise")){
        Cube.Updateup3();
      } else if(Command.command.equals("back1_Counterclockwise")){
        Cube.Update_Counterclockwise_back1();
      } else if(Command.command.equals("back2_Counterclockwise")){
        Cube.Update_Counterclockwise_back2();
      } else if(Command.command.equals("back3_Counterclockwise")){
        Cube.Update_Counterclockwise_back3();
      } else if(Command.command.equals("left1_Counterclockwise")){
        Cube.Update_Counterclockwise_left1();
      } else if(Command.command.equals("left2_Counterclockwise")){
        Cube.Update_Counterclockwise_left2();
      } else if(Command.command.equals("left3_Counterclockwise")){
        Cube.Update_Counterclockwise_left3();
      } else if(Command.command.equals("down1_Counterclockwise")){
        Cube.Update_Counterclockwise_down1();
      } else if(Command.command.equals("down2_Counterclockwise")){
        Cube.Update_Counterclockwise_down2();
      } else if(Command.command.equals("down3_Counterclockwise")){
        Cube.Update_Counterclockwise_down3();
      } else if(Command.command.equals("front1_Counterclockwise")){
        Cube.Update_Counterclockwise_front1();
      } else if(Command.command.equals("front2_Counterclockwise")){
        Cube.Update_Counterclockwise_front2();
      } else if(Command.command.equals("front3_Counterclockwise")){
        Cube.Update_Counterclockwise_front3();
      } else if(Command.command.equals("right1_Counterclockwise")){
        Cube.Update_Counterclockwise_right1();
      } else if(Command.command.equals("right2_Counterclockwise")){
        Cube.Update_Counterclockwise_right2();
      } else if(Command.command.equals("right3_Counterclockwise")){
        Cube.Update_Counterclockwise_right3();
      } else if(Command.command.equals("up1_Counterclockwise")){
        Cube.Update_Counterclockwise_up1();
      } else if(Command.command.equals("up2_Counterclockwise")){
        Cube.Update_Counterclockwise_up2();
      } else if(Command.command.equals("up3_Counterclockwise")){
        Cube.Update_Counterclockwise_up3();
      } 
    }
  }

  void Updateright3(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];

    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[0][m][n].upFace;
        this.cubebox[0][m][n].upFace    = this.cubebox[0][m][n].frontFace;
        this.cubebox[0][m][n].frontFace  = this.cubebox[0][m][n].downFace;
        this.cubebox[0][m][n].downFace  = this.cubebox[0][m][n].backFace;
        this.cubebox[0][m][n].backFace = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[0][m][n];
      }
    }

    for(int m=0;m<3;m++){
      for(int n=2;n>=0;n--){
        this.cubebox[0][n][m] = tmpColorArr[m*3+2-n];
      }
    }
  }

  void Updateright2(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];

    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[1][m][n].upFace;
        this.cubebox[1][m][n].upFace    = this.cubebox[1][m][n].frontFace;
        this.cubebox[1][m][n].frontFace = this.cubebox[1][m][n].downFace;
        this.cubebox[1][m][n].downFace  = this.cubebox[1][m][n].backFace;
        this.cubebox[1][m][n].backFace  = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[1][m][n];
      }
    }

    for(int m=0;m<3;m++){
      for(int n=2;n>=0;n--){
        this.cubebox[1][n][m] = tmpColorArr[m*3+2-n];
      }
    }
  }

  void Updateright1(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];

    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[2][m][n].upFace;
        this.cubebox[2][m][n].upFace    = this.cubebox[2][m][n].frontFace;
        this.cubebox[2][m][n].frontFace  = this.cubebox[2][m][n].downFace;
        this.cubebox[2][m][n].downFace  = this.cubebox[2][m][n].backFace;
        this.cubebox[2][m][n].backFace = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[2][m][n];
      }
    }

    for(int m=0;m<3;m++){
      for(int n=2;n>=0;n--){
        this.cubebox[2][n][m] = tmpColorArr[m*3+2-n];
      }
    }
  }

  void Update_Counterclockwise_right3(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];

    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[0][m][n].upFace;
        this.cubebox[0][m][n].upFace    = this.cubebox[0][m][n].backFace;
        this.cubebox[0][m][n].backFace  = this.cubebox[0][m][n].downFace;
        this.cubebox[0][m][n].downFace  = this.cubebox[0][m][n].frontFace;
        this.cubebox[0][m][n].frontFace = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[0][m][n];
      }
    }

    for(int m=2;m>=0;m--){
      for(int n=0;n<3;n++){
        this.cubebox[0][n][m] = tmpColorArr[(2-m)*3+n];
      }
    }
  }

  void Update_Counterclockwise_right2(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];

    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[1][m][n].upFace;
        this.cubebox[1][m][n].upFace    = this.cubebox[1][m][n].backFace;
        this.cubebox[1][m][n].backFace  = this.cubebox[1][m][n].downFace;
        this.cubebox[1][m][n].downFace  = this.cubebox[1][m][n].frontFace;
        this.cubebox[1][m][n].frontFace = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[1][m][n];
      }
    }

    for(int m=2;m>=0;m--){
      for(int n=0;n<3;n++){
        this.cubebox[1][n][m] = tmpColorArr[(2-m)*3+n];
      }
    }
  }

  void Update_Counterclockwise_right1(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];

    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[2][m][n].upFace;
        this.cubebox[2][m][n].upFace    = this.cubebox[2][m][n].backFace;
        this.cubebox[2][m][n].backFace  = this.cubebox[2][m][n].downFace;
        this.cubebox[2][m][n].downFace  = this.cubebox[2][m][n].frontFace;
        this.cubebox[2][m][n].frontFace = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[2][m][n];
      }
    }

    for(int m=2;m>=0;m--){
      for(int n=0;n<3;n++){
        this.cubebox[2][n][m] = tmpColorArr[(2-m)*3+n];
      }
    }
  }

  void Updateback1(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];
    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[m][n][0].upFace;
        this.cubebox[m][n][0].upFace    = this.cubebox[m][n][0].leftFace;
        this.cubebox[m][n][0].leftFace  = this.cubebox[m][n][0].downFace;
        this.cubebox[m][n][0].downFace  = this.cubebox[m][n][0].rightFace;
        this.cubebox[m][n][0].rightFace = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[m][n][0];
      }
    }

    for(int m=0;m<3;m++){
      for(int n=2;n>=0;n--){
        this.cubebox[n][m][0] = tmpColorArr[(m)*3+2-n];
      }
    }
  }

  void Updateback2(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];
    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[m][n][1].upFace;
        this.cubebox[m][n][1].upFace    = this.cubebox[m][n][1].leftFace;
        this.cubebox[m][n][1].leftFace  = this.cubebox[m][n][1].downFace;
        this.cubebox[m][n][1].downFace  = this.cubebox[m][n][1].rightFace;
        this.cubebox[m][n][1].rightFace = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[m][n][1];
      }
    }

    for(int m=0;m<3;m++){
      for(int n=2;n>=0;n--){
        this.cubebox[n][m][1] = tmpColorArr[(m)*3+2-n];
      }
    }
  }

  void Updateback3(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];
    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[m][n][2].upFace;
        this.cubebox[m][n][2].upFace    = this.cubebox[m][n][2].leftFace;
        this.cubebox[m][n][2].leftFace  = this.cubebox[m][n][2].downFace;
        this.cubebox[m][n][2].downFace  = this.cubebox[m][n][2].rightFace;
        this.cubebox[m][n][2].rightFace = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[m][n][2];
      }
    }

    for(int m=0;m<3;m++){
      for(int n=2;n>=0;n--){
        this.cubebox[n][m][2] = tmpColorArr[(m)*3+2-n];
      }
    }
  }

  void Update_Counterclockwise_back1(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];
    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[m][n][0].upFace;
        this.cubebox[m][n][0].upFace    = this.cubebox[m][n][0].rightFace;
        this.cubebox[m][n][0].rightFace = this.cubebox[m][n][0].downFace;
        this.cubebox[m][n][0].downFace  = this.cubebox[m][n][0].leftFace;
        this.cubebox[m][n][0].leftFace  = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[m][n][0];
      }
    }

    for(int m=2;m>=0;m--){
      for(int n=0;n<3;n++){
        this.cubebox[n][m][0] = tmpColorArr[(2-m)*3+n];
      }
    }
  }

  void Update_Counterclockwise_back2(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];
    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[m][n][1].upFace;
        this.cubebox[m][n][1].upFace    = this.cubebox[m][n][1].rightFace;
        this.cubebox[m][n][1].rightFace = this.cubebox[m][n][1].downFace;
        this.cubebox[m][n][1].downFace  = this.cubebox[m][n][1].leftFace;
        this.cubebox[m][n][1].leftFace  = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[m][n][1];
      }
    }

    for(int m=2;m>=0;m--){
      for(int n=0;n<3;n++){
        this.cubebox[n][m][1] = tmpColorArr[(2-m)*3+n];
      }
    }
  }

  void Update_Counterclockwise_back3(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];
    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[m][n][2].upFace;
        this.cubebox[m][n][2].upFace    = this.cubebox[m][n][2].rightFace;
        this.cubebox[m][n][2].rightFace = this.cubebox[m][n][2].downFace;
        this.cubebox[m][n][2].downFace  = this.cubebox[m][n][2].leftFace;
        this.cubebox[m][n][2].leftFace  = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[m][n][2];
      }
    }

    for(int m=2;m>=0;m--){
      for(int n=0;n<3;n++){
        this.cubebox[n][m][2] = tmpColorArr[(2-m)*3+n];
      }
    }
  }

  void Updateup1(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];
    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[n][0][m].rightFace;
        this.cubebox[n][0][m].rightFace = this.cubebox[n][0][m].frontFace;
        this.cubebox[n][0][m].frontFace = this.cubebox[n][0][m].leftFace;
        this.cubebox[n][0][m].leftFace  = this.cubebox[n][0][m].backFace;
        this.cubebox[n][0][m].backFace  = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[n][0][m];
      }
    }

    for(int m=0;m<3;m++){
      for(int n=2;n>=0;n--){
        this.cubebox[m][0][n] = tmpColorArr[m*3+(2-n)];
      }
    }
  }

  void Updateup2(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];
    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[n][1][m].rightFace;
        this.cubebox[n][1][m].rightFace  = this.cubebox[n][1][m].frontFace;
        this.cubebox[n][1][m].frontFace  = this.cubebox[n][1][m].leftFace;
        this.cubebox[n][1][m].leftFace   = this.cubebox[n][1][m].backFace;
        this.cubebox[n][1][m].backFace   = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[n][1][m];
      }
    }

    for(int m=0;m<3;m++){
      for(int n=2;n>=0;n--){
        this.cubebox[m][1][n] = tmpColorArr[m*3+(2-n)];
      }
    }
  }

  void Updateup3(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];
    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[n][2][m].rightFace;
        this.cubebox[n][2][m].rightFace  = this.cubebox[n][2][m].frontFace;
        this.cubebox[n][2][m].frontFace  = this.cubebox[n][2][m].leftFace;
        this.cubebox[n][2][m].leftFace   = this.cubebox[n][2][m].backFace;
        this.cubebox[n][2][m].backFace   = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[n][2][m];
      }
    }

    for(int m=0;m<3;m++){
      for(int n=2;n>=0;n--){
        this.cubebox[m][2][n] = tmpColorArr[m*3+(2-n)];
      }
    }
  }

  void Update_Counterclockwise_up1(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];
    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[n][0][m].rightFace;
        this.cubebox[n][0][m].rightFace = this.cubebox[n][0][m].backFace;
        this.cubebox[n][0][m].backFace = this.cubebox[n][0][m].leftFace;
        this.cubebox[n][0][m].leftFace  = this.cubebox[n][0][m].frontFace;
        this.cubebox[n][0][m].frontFace  = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[n][0][m];
      }
    }

    for(int m=2;m>=0;m--){
      for(int n=0;n<3;n++){
        this.cubebox[m][0][n] = tmpColorArr[(2-m)*3+n];
      }
    }
  }

  void Update_Counterclockwise_up2(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];
    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[n][1][m].rightFace;
        this.cubebox[n][1][m].rightFace  = this.cubebox[n][1][m].backFace;
        this.cubebox[n][1][m].backFace  = this.cubebox[n][1][m].leftFace;
        this.cubebox[n][1][m].leftFace   = this.cubebox[n][1][m].frontFace;
        this.cubebox[n][1][m].frontFace   = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[n][1][m];
      }
    }

    for(int m=2;m>=0;m--){
      for(int n=0;n<3;n++){
        this.cubebox[m][1][n] = tmpColorArr[(2-m)*3+n];
      }
    }
  }

  void Update_Counterclockwise_up3(){
    boxTemplate [] tmpColorArr = new boxTemplate[9];
    for(int m=0;m<3;m++){
      for(int n=0;n<3;n++){
        String tmpcolor = this.cubebox[n][2][m].rightFace;
        this.cubebox[n][2][m].rightFace  = this.cubebox[n][2][m].backFace;
        this.cubebox[n][2][m].backFace  = this.cubebox[n][2][m].leftFace;
        this.cubebox[n][2][m].leftFace   = this.cubebox[n][2][m].frontFace;
        this.cubebox[n][2][m].frontFace   = tmpcolor;
        tmpColorArr[m*3+n] = this.cubebox[n][2][m];
      }
    }

    for(int m=2;m>=0;m--){
      for(int n=0;n<3;n++){
        this.cubebox[m][2][n] = tmpColorArr[(2-m)*3+n];
      }
    }
  }

  /*
    because Cube it is symmetric
    left1 is equal to right3
    left2 is equal to right2
    left3 is equal to right1
  */
  void Updateleft1(){this.Updateright3();}
  void Updateleft2(){this.Updateright2();}
  void Updateleft3(){this.Updateright1();}

  void Updatefront1(){this.Updateback3();}
  void Updatefront2(){this.Updateback2();}
  void Updatefront3(){this.Updateback1();}

  void Updatedown1(){this.Updateup3();}
  void Updatedown2(){this.Updateup2();}
  void Updatedown3(){this.Updateup1();}
  
  void Update_Counterclockwise_left1(){this.Update_Counterclockwise_right3();}
  void Update_Counterclockwise_left2(){this.Update_Counterclockwise_right2();}
  void Update_Counterclockwise_left3(){this.Update_Counterclockwise_right1();}

  void Update_Counterclockwise_front1(){this.Update_Counterclockwise_back3();}
  void Update_Counterclockwise_front2(){this.Update_Counterclockwise_back2();}
  void Update_Counterclockwise_front3(){this.Update_Counterclockwise_back1();}

  void Update_Counterclockwise_down1(){this.Update_Counterclockwise_up3();}
  void Update_Counterclockwise_down2(){this.Update_Counterclockwise_up2();}
  void Update_Counterclockwise_down3(){this.Update_Counterclockwise_up1();}
}
