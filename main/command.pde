class commandTemplate{

	String[] 	commandfile 	;
	String 		command			;
	boolean 	fileMutex		;
	boolean 	processMutex	;

	commandTemplate(){
		this.command 			= ""	;
		this.fileMutex 			= false	;
		this.processMutex 		= true	;
	}
    
	void enable(String commandstr){
		if(commandstr.equals("back1_clockwise")){
				Cube.back1_clockwise	= true;
		} else if(commandstr.equals("back2_clockwise")){
				Cube.back2_clockwise 	= true;
		} else if(commandstr.equals("back3_clockwise")){
				Cube.back3_clockwise 	= true;
		} else if(commandstr.equals("left1_clockwise")){
				Cube.left1_clockwise 	= true;
		} else if(commandstr.equals("left2_clockwise")){
				Cube.left2_clockwise 	= true;
		} else if(commandstr.equals("left3_clockwise")){
				Cube.left3_clockwise 	= true;
		} else if(commandstr.equals("down1_clockwise")){
				Cube.down1_clockwise	= true;
		} else if(commandstr.equals("down2_clockwise")){
				Cube.down2_clockwise 	= true;
		} else if(commandstr.equals("down3_clockwise")){
				Cube.down3_clockwise 	= true;
		} else if(commandstr.equals("front1_clockwise")){
				Cube.front1_clockwise = true;
		} else if(commandstr.equals("front2_clockwise")){
				Cube.front2_clockwise = true;
		} else if(commandstr.equals("front3_clockwise")){
				Cube.front3_clockwise = true;
		} else if(commandstr.equals("right1_clockwise")){
				Cube.right1_clockwise = true;
		} else if(commandstr.equals("right2_clockwise")){
				Cube.right2_clockwise = true;
		} else if(commandstr.equals("right3_clockwise")){
				Cube.right3_clockwise = true;
		} else if(commandstr.equals("up1_clockwise")){
				Cube.up1_clockwise 		= true;
		} else if(commandstr.equals("up2_clockwise")){
				Cube.up2_clockwise 		= true;
		} else if(commandstr.equals("up3_clockwise")){
				Cube.up3_clockwise 		= true;
		} else if(commandstr.equals("back1_Counterclockwise")){
				Cube.back1_Counterclockwise 	= true;
		} else if(commandstr.equals("back2_Counterclockwise")){
				Cube.back2_Counterclockwise 	= true;
		} else if(commandstr.equals("back3_Counterclockwise")){
				Cube.back3_Counterclockwise 	= true;
		} else if(commandstr.equals("left1_Counterclockwise")){
				Cube.left1_Counterclockwise 	= true;
		} else if(commandstr.equals("left2_Counterclockwise")){
				Cube.left2_Counterclockwise 	= true;
		} else if(commandstr.equals("left3_Counterclockwise")){
				Cube.left3_Counterclockwise 	= true;
		} else if(commandstr.equals("down1_Counterclockwise")){
				Cube.down1_Counterclockwise		= true;
		} else if(commandstr.equals("down2_Counterclockwise")){
				Cube.down2_Counterclockwise 	= true;
		} else if(commandstr.equals("down3_Counterclockwise")){
				Cube.down3_Counterclockwise 	= true;
		} else if(commandstr.equals("front1_Counterclockwise")){
				Cube.front1_Counterclockwise 	= true;
		} else if(commandstr.equals("front2_Counterclockwise")){
				Cube.front2_Counterclockwise 	= true;
		} else if(commandstr.equals("front3_Counterclockwise")){
				Cube.front3_Counterclockwise 	= true;
		} else if(commandstr.equals("right1_Counterclockwise")){
				Cube.right1_Counterclockwise 	= true;
		} else if(commandstr.equals("right2_Counterclockwise")){
				Cube.right2_Counterclockwise 	= true;
		} else if(commandstr.equals("right3_Counterclockwise")){
				Cube.right3_Counterclockwise 	= true;
		} else if(commandstr.equals("up1_Counterclockwise")){
				Cube.up1_Counterclockwise 		= true;
		} else if(commandstr.equals("up2_Counterclockwise")){
				Cube.up2_Counterclockwise 		= true;
		} else if(commandstr.equals("up3_Counterclockwise")){
				Cube.up3_Counterclockwise 		= true;
		} else if(commandstr.equals("up_right")){
			Cube.up_right 					= true;
			Cube.front1_clockwise  		 	= true;
			Cube.front2_clockwise 		 	= true;
			Cube.front3_clockwise 		 	= true;
		} else if(commandstr.equals("up_left")){
			Cube.up_left 					= true;
			Cube.front1_Counterclockwise 	= true;
			Cube.front2_Counterclockwise 	= true;
			Cube.front3_Counterclockwise 	= true;
		} else if(commandstr.equals("up_back")){
			Cube.up_back 					= true;
			Cube.left1_clockwise 			= true;
			Cube.left2_clockwise 			= true;
			Cube.left3_clockwise 			= true;
		} else if(commandstr.equals("up_front")){
			Cube.up_front 					= true;
			Cube.left1_Counterclockwise 	= true;
			Cube.left2_Counterclockwise 	= true;
			Cube.left3_Counterclockwise 	= true;
		} else if(commandstr.equals("up_fix_right")){
			Cube.up_fix_right 				= true;
			Cube.up1_Counterclockwise 	= true;
			Cube.up2_Counterclockwise 	= true;
			Cube.up3_Counterclockwise 	= true;
		} else if(commandstr.equals("up_fix_left")){
			Cube.up_fix_left 				= true;
			Cube.up1_clockwise 			= true;
			Cube.up2_clockwise 			= true;
			Cube.up3_clockwise 			= true;
		}
	}

	void disable(){
		Cube.back1_clockwise 			= false ;
		Cube.back2_clockwise 			= false ;
		Cube.back3_clockwise 			= false ;
		Cube.left1_clockwise 			= false ;
		Cube.left2_clockwise 			= false ;
		Cube.left3_clockwise 			= false ;
		Cube.down1_clockwise 			= false ;
		Cube.down2_clockwise 			= false ;
		Cube.down3_clockwise 			= false ;
		Cube.front1_clockwise 			= false ; 
		Cube.front2_clockwise 			= false ;
		Cube.front3_clockwise 			= false ;
		Cube.right1_clockwise 			= false ;
		Cube.right2_clockwise 			= false ;
		Cube.right3_clockwise 			= false ;
		Cube.up1_clockwise 				= false ;
		Cube.up2_clockwise 				= false ;
		Cube.up3_clockwise 				= false ;

		Cube.back1_Counterclockwise 	= false ;
		Cube.back2_Counterclockwise 	= false ;
		Cube.back3_Counterclockwise 	= false ;
		Cube.left1_Counterclockwise 	= false ;
		Cube.left2_Counterclockwise 	= false ;
		Cube.left3_Counterclockwise 	= false ;
		Cube.down1_Counterclockwise 	= false ;
		Cube.down2_Counterclockwise 	= false ;
		Cube.down3_Counterclockwise 	= false ;
		Cube.front1_Counterclockwise 	= false ;
		Cube.front2_Counterclockwise 	= false ;
		Cube.front3_Counterclockwise 	= false ;
		Cube.right1_Counterclockwise 	= false ;
		Cube.right2_Counterclockwise 	= false ;
		Cube.right3_Counterclockwise 	= false ;
		Cube.up1_Counterclockwise 		= false ;
		Cube.up2_Counterclockwise 		= false ;
		Cube.up3_Counterclockwise 		= false ;

		Cube.up_right                   = false ;
		Cube.up_left                    = false ;
		Cube.up_back                    = false ;
		Cube.up_front                   = false ;
		Cube.up_fix_right               = false ;
		Cube.up_fix_left                = false ;
	}

	void read(){
		this.commandfile = loadStrings("../sol/command.txt");
		if(this.commandfile.length==0){
			this.fileMutex = false;
			// Debug.formatprintcolor();
			// Debug.printcolor();
			// exit();
		} else {
			this.command = this.commandfile[0];
			this.fileMutex = true;
		}
	}

	void clear(){
		this.command = "";
		PrintWriter outputfile;
		outputfile = createWriter("../sol/command.txt");
		for(int i=1;i<this.commandfile.length;i++){
			outputfile.println(commandfile[i]);
		}
		outputfile.flush();
		outputfile.close();
		this.disable();
	}
}