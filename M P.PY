from tkinter import *
Math=Tk()
Math.config(bg="black")
def Laptop():
    m=Tk()
    m.config(bg="black")
    m.geometry("700x1400")
    m.title("Math Project For Mobile")
    Label(m,text="Surface Area & Volume",bg="black",fg="white",font="arial 15 bold underline").pack()
    def Triangle():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1400")
        main.title("TRIANGLE")
        def Area_of_a_Right_Angled_Triangle():
            def a1():
                a3=int(B2.get())
                a4=int(H2.get())
                a=(1/2*a3*a4)
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            Label(main,text="Enter the base",bg="black",fg="yellow",width=60,font=15).pack()
            B2=Entry(main,bg="lightblue")
            B2.pack()
            Label(main,text="Enter the height",bg="black",fg="yellow",width=60,font=15).pack()
            H2=Entry(main,bg="lightblue")
            H2.pack()
            Button(main,text="Answer",command=a1,bg="darkgreen",fg="White",font=15).pack()
        def Area_of_an_Equilateral_Triangle():
            def a2():
                a5=int(s2.get())
                a=((3**0.5/4)*(a5)*(a5))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            Label(main,text="Enter the side",bg="black",fg="yellow",width=60,font=15).pack()
            s2=Entry(main,bg="lightblue")
            s2.pack()
            Button(main,text="Answer",command=a2,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Triangle",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
    
        Label(main,text=" What is a Triangle ?  ",bg="black",fg="yellow",width=60,font="arial 10 ").pack()
        def trians():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1400")
            main2.title("TRIANGLE")
            Label(main2,text=" What is a Triangle ?  ",bg="black",fg="yellow",width=60,font="arial 10 ").pack()
            Label(main2,text="-> A triangle is a closed, 2-dimensional shape \nwith 3 sides, 3 angles, and 3 vertices.\n-> A triangle is also a polygon.Internal angle:\n 60° & Sum of interior angles: 1140°\n We postulate the triangle principle which\n states that any information distance is\n well defined on any pair of measurements,\n even if the  two measurements cannot be jointly\n performed.\n-> As a consequence,  the triangle inequality for\n this distance is  obeyed for any\n three measurements.",bg="black",fg="white",font=15).pack()
            main2.mainloop()
        Button(main,text="Answer",command=trians,bg="darkgreen",fg="White",font=15).pack()
        
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        
        
        Label(main,text="Area of a Right Angled Triangle",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text=" ½ × Base × Height ",bg="black",fg="white",width=60,font=15).pack()
        B2=Button(main,text="Find",command=Area_of_a_Right_Angled_Triangle,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Area of an Equilateral Triangle",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text=" (√3)/4 × side*side",bg="black",fg="white",width=60,font=15).pack()
        
        B3=Button(main,text="Find",command=Area_of_an_Equilateral_Triangle,bg="darkgreen",fg="White",font=15).pack()
        main.mainloop()
        
        
        
        
        
        
        
        
        
        
        
    def Rectangular_Prism():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1400")
        main.title("RECTANGULAR PRISM")
        def Surface_Area_of_a_Rectangular_Prism():
            def area():
                a1=int(R1.get())
                a2=int(W1.get())
                a=(2*(a1+a2))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            Label(main,text="Enter the Length",bg="black",fg="yellow",width=60,font=15).pack()
            R1=Entry(main,bg="lightblue")
            R1.pack()
            Label(main,text="Enter the Width ",bg="black",fg="yellow",width=60,font=15).pack()
            W1=Entry(main,bg="lightblue")
            W1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White",font=15).pack()
        def Total_Surface_Area_rectangular_prism():
            def a1():
                a3=int(L2.get())
                a4=int(W2.get())
                a5=int(H2.get())
                a=(2*(a3*a5)+(a4*a5)+(a3*a4))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            Label(main,text="Enter the Length ",bg="black",fg="yellow",width=60,font=15).pack()
            L2=Entry(main,bg="lightblue")
            L2.pack()
            Label(main,text="Enter the Width ",bg="black",fg="yellow",width=60,font=15).pack()
            W2=Entry(main,bg="lightblue")
            W2.pack()
            Label(main,text="Enter the Height",bg="black",fg="yellow",width=60,font=15).pack()
            H2=Entry(main,bg="lightblue")
            H2.pack()
            Button(main,text="Answer",command=a1,bg="darkgreen",fg="White",font=15).pack()
        def volume_of_a_rectangular_prism():
            def v1():
                v1=int(v4.get())
                v2=int(v5.get())
                v3=int(v6.get())
                a=(v1*v2*v3)
                ans=str(a)
                Label(main,text="Your Volume  is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            Label(main,text="Enter the Length",bg="black",fg="yellow",width=60,font=15).pack()
            v4=Entry(main,bg="lightblue")
            v4.pack()
            Label(main,text="Enter the Width ",bg="black",fg="yellow",width=60,font=15).pack()
            v5=Entry(main,bg="lightblue")
            v5.pack()
            Label(main,text="Enter the Height",bg="black",fg="yellow",width=60,font=15).pack()
            v6=Entry(main,bg="lightblue")
            v6.pack()
            Button(main,text="Answer",command=v1,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Rectangular Prism",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
        
    
        Label(main,text=" What is a Rectangular Prism ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        def op():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1400")
            main2.title("RECTANGULAR PRISM")
            Label(main2,text=" What is a Rectangular Prism ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
            
            Label(main2,text="->In geometry, a rectangular prism is\n a polyhedron with two congruent \n and parallel bases. It is also called a cuboid.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->A rectangular prism is a three-\ndimensional shape, that has six faces \n (two at the top and bottom and four are\n lateral faces). All the faces of the prism \n  are rectangular in shape.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->A rectangular prism is a three-dimensional\n object. Hence, it will have its \n surface area and volume. To calculate the\n volume and surface area of a prism, \n we have to know the length of its sides or edges.\nLet ‘l’, ‘w’ and ‘h’ be the length, \n  width and height of the rectangular prism.",bg="black",fg="white",width=60,font=15).pack()
            main2.mainloop()
        Button(main,text="Answer",command=op,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        Label(main,text="Surface Area of Rectangular Prism",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text=" 2 (length + width)",bg="black",fg="white",width=60,font=15).pack()
        B1=Button(main,text="Find",command=Surface_Area_of_a_Rectangular_Prism,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Total Surface Area  of Rectangular Prism",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text=" 2 (length.height +width.height + length.width )",bg="black",fg="white",width=60,font=15).pack()
        B2=Button(main,text="Find",command=Total_Surface_Area_rectangular_prism,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Volume of a Rectangular Prism",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text="length*width*height",bg="black",fg="white",width=60,font=15).pack()
        
        
        
        B3=Button(main,text="Find",command=volume_of_a_rectangular_prism,bg="darkgreen",fg="White",font=15).pack()
        main.mainloop()
    def Cone():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1400")
        main.title("CONE")
        def Surface_Area_of_Cone():
            def area():
                a1=int(R1.get())
                a2=int(H1.get())
                l1=((a1)*(a1)+(a2)*(a2))
                l=(l1**0.5)
                a=((3.14)*(a1)*(a1+l))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60,font=15).pack()
            R1=Entry(main,bg="lightblue")
            R1.pack()
            Label(main,text="Enter the height",bg="black",fg="yellow",width=60,font=15).pack()
            H1=Entry(main,bg="lightblue")
            H1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White",font=15).pack()
        def Volume_of_Cone():
            def v1():
                a3=int(R2.get())
                a4=int(H2.get())
                a=(1/3*(3.14)*(a3)*(a3)*(a4))
                ans=str(a)
                Label(main,text="Your Volume is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60,font=15).pack()
            R2=Entry(main,bg="lightblue")
            R2.pack()
            Label(main,text="Enter the height",bg="black",fg="yellow",width=60,font=15).pack()
            H2=Entry(main,bg="lightblue")
            H2.pack()
            Button(main,text="Answer",command=v1,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Cone.",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
    
        Label(main,text=" What is a Cone ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        def mar():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1400")
            main2.title("CONE")
            Label(main2,text=" What is a Cone ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
            Label(main2,text="->A cone is a three-dimensional shape\n in geometry that narrows smoothly \n from a flat base (usually circular base) to a\n point(which forms an axis to the \n centre of base) called the apex or vertex.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->These cones are also stated \nas a circular cone.",bg="black",fg="white",width=60,font=15).pack()
            main2.mainloop()
        Button(main,text="Answer",command=mar,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        Label(main,text="Surface Area of the Cone",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text=" π.radius(length + radius)",bg="black",fg="white",width=60,font=15).pack()
        B1=Button(main,text="Find",command=Surface_Area_of_Cone,bg="darkgreen",fg="White",font=15).pack()
        
        Label(main,text="Volume of the Cone",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text="  ⅓ π.radius*radius.height",bg="black",fg="white",width=60,font=15).pack()
    
        
        B2=Button(main,text="Find",command=Volume_of_Cone,bg="darkgreen",fg="White",font=15).pack()
        main.mainloop()
    def Rectangle():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1400")
        main.title("RECTANGLE")
        def Area_of_Rectangle():
            def area():
                a1=int(L1.get())
                a2=int(W1.get())
                a=((a1)*(a2))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            
            Label(main,text="Enter the Length",bg="black",fg="yellow",width=60,font=15).pack()
            L1=Entry(main,bg="lightblue")
            L1.pack()
            Label(main,text="Enter the Width",bg="black",fg="yellow",width=60,font=15).pack()
            W1=Entry(main,bg="lightblue")
            W1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Rectangle",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
    
        Label(main,text=" What is a Rectangle ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1400")
            main2.title("RECTANGLE")
            Label(main2,text=" What is a Rectangle ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
            Label(main2,text="->A Rectangle is a four sided-polygon,\n having all the internal angles equal \n to 90 degrees. ",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->A rectangle is characterized by length (L)\n and width (W). Both length \n and width are different in size.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->Sum of all interior angles equal to 360 degrees.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->The opposite sides are equal and parallel.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->It’s a parallelogram with four right angles.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->Area is equal to product of its length\n and breadth.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->It has four sides and four vertices.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->The most common everyday things or\n objects we see and are rectangular \n in shape is Television, computer screen,\n notebook, mobile phones, CPU , \n Notice boards,Table, Book, TV screen,\n Mobile phone, Wall, Magazine, \n Tennis court, etc.",bg="black",fg="white",width=60,font=15).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        Label(main,text="Area of Rectangle",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text="length*width",bg="black",fg="white",width=60,font=15).pack()
        
        B1=Button(main,text="Find",command=Area_of_Rectangle,bg="darkgreen",fg="White",font=15).pack()
        main.mainloop()
    def Square():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1400")
        main.title("SQUARE")
        def Area_of_Square():
            def area():
                a1=int(L1.get())
                a=((a1)*(a1))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            
            Label(main,text="Enter the Side",bg="black",fg="yellow",width=60,font=15).pack()
            L1=Entry(main,bg="lightblue")
            L1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Square",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
    
        Label(main,text=" What is a Square ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1400")
            main2.title("RECTANGLE")
        
            Label(main2,text=" What is a Square ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
            Label(main2,text="->Square is a regular quadrilateral",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->a square where all the sides are\n equal and each angle equals 90 degrees.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->The length of diagonals is greater\n than the sides of the square.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->The diagonals of the square\n bisect each other at 90°.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->All four sides of the square are congruent\n or equal to each other.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->The diagonal of the square divide it\n into two similar isosceles triangles.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->There are many examples of square shape\n in real-life such as a square plot \n or field, a square-shaped ground, square\n-shaped table cloth, the tiles of \n the floor in square shape, etc.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->A square is a four-sided polygon, whose\n all its sides are equal in length and \n opposite sides are parallel  to each other.\n Also, each vertices of square \n have angle equal to 90 degrees.",bg="black",fg="white",width=60,font=15).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        Label(main,text="Area of square",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text="side*side",bg="black",fg="white",width=60,font=15).pack()
        
        B1=Button(main,text="Find",command=Area_of_Square,bg="darkgreen",fg="White",font=15).pack()
        main.mainloop()
    def Cuboid():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1400")
        main.title("CUBOID")
        def Cuboid_Area():
            def area():
                a1=int(L1.get())
                a2=int(B1.get())
                a3=int(H1.get())
                a=(2*a3)*(a1+a2)
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            
            Label(main,text="Enter the Length",bg="black",fg="yellow",width=60,font=15).pack()
            L1=Entry(main,bg="lightblue")
            L1.pack()
            Label(main,text="Enter the breath",bg="black",fg="yellow",width=60,font=15).pack()
            B1=Entry(main,bg="lightblue")
            B1.pack()
            Label(main,text="Enter the Height",bg="black",fg="yellow",width=60,font=15).pack()
            H1=Entry(main,bg="lightblue")
            H1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White",font=15).pack()
        def Cuboid_T_Area():
            def a2():
                a1=int(L1.get())
                a2=int(B1.get())
                a3=int(H1.get())
                a=2*((a1*a2)+(a2*a3)+(a1*a3))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()               
            Label(main,text="Enter the Length",bg="black",fg="yellow",width=60,font=15).pack()
            L1=Entry(main,bg="lightblue")
            L1.pack()
            Label(main,text="Enter the breath",bg="black",fg="yellow",width=60,font=15).pack()
            B1=Entry(main,bg="lightblue")
            B1.pack()
            Label(main,text="Enter the Height",bg="black",fg="yellow",width=60,font=15).pack()
            H1=Entry(main,bg="lightblue")
            H1.pack()
            Button(main,text="Answer",command=a2,bg="darkgreen",fg="White",font=15).pack()
    
        Label(main,text="Cuboid",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
        Label(main,text=" What is a Cuboid ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        
        
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1400")
            main2.title("CUBOID")
            Label(main2,text=" What is a Cuboid ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
            Label(main2,text="->A cuboid is a three dimensional\n solid that has 6 faces (rectangular), \n  14 vertices and 14 edges. A cuboid has\n three dimensions such as length, width \n and height. A perfect  cuboid is said\n to be a cuboid that has integer edges.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->Cuboid has three dimensions:\n length, width and height.",bg="black",fg="white",width=60,font=15).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        Label(main,text="Cuboid Lateral Surface Area",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text="2.height(length + width)",bg="black",fg="white",width=60,font=15).pack()
        B1=Button(main,text="Find",command=Cuboid_Area,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Cuboid Total Surface Area.",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text="2.(length.width + width.height + height.length)",bg="black",fg="white",width=60,font=15).pack()
      
        
        B2=Button(main,text="Find",command=Cuboid_T_Area,bg="darkgreen",fg="White",font=15).pack()
        main.mainloop()
    def Cube():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1400")
        main.title("CUBE")
        def Area_of_one_face_cube():
            def area():
                a1=int(L1.get())
                a=((a1)*(a1))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()       
            Label(main,text="Enter the Side",bg="black",fg="yellow",width=60,font=15).pack()
            L1=Entry(main,bg="lightblue")
            L1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White",font=15).pack()
        def Lateral_surface_area_cube():
            def a2():
                a1=int(L2.get())
                a=(4*(a1)*(a1))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()               
            Label(main,text="Enter the side",bg="black",fg="yellow",width=60,font=15).pack()
            L2=Entry(main,bg="lightblue")
            L2.pack()
            Button(main,text="Answer",command=a2,bg="darkgreen",fg="White",font=15).pack()
    
        Label(main,text="Cube",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
        
        Label(main,text=" What is a Cube ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1400")
            main2.title("CUBE")
            Label(main2,text=" What is a Cube ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
            Label(main2,text="->As discussed earlier,\n a cube is a 3-D.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->solid shape, which has 6 faces.\n A cube is one of the simplest shapes in three \n dimensional space. All the six faces of \na cube are squares, a twodimensional  \n shape.",bg="black",fg="white",width=60,font=15).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        Label(main,text="One face Area",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text=" side*side",bg="black",fg="white",width=60,font=15).pack()
        B1=Button(main,text="Find",command=Area_of_one_face_cube,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Lateral surface of Cube",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text="4*side*side",bg="black",fg="white",width=60,font=15).pack()
    
        
        B2=Button(main,text="Find",command=Lateral_surface_area_cube,bg="darkgreen",fg="White",font=15).pack()
        main.mainloop()
    def Sphere():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1400")
        main.title("SPHERE")
        def Surface_Area_of_a_Sphere():
            def area():
                a1=int(R1.get())
                a=(4*(3.14)*(a1)*(a1))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60,font=15).pack()
            R1=Entry(main,bg="lightblue")
            R1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White",font=15).pack()
        def Volume_of_a_Sphere():
            def a1():
                    a2=int(R2.get())
                    a=(4/3*(3.14)*(a2)*(a2)*(a2))
                    ans=str(a)
                    Label(main,text="Your Volume is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60,font=15).pack()
            R2=Entry(main,bg="lightblue")
            R2.pack()
            Button(main,text="Answer",command=a1,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Sphere",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
        
        Label(main,text=" What is a Sphere ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1400")
            main2.title("SPHERE")
            Label(main2,text=" What is a Sphere ?",bg="black",fg="yellow",width=60,font="arial 15").pack()
            Label(main2,text="->A sphere is a three-dimensional\n object that is round in shape.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->A sphere does not have any edges\n or vertices, like other 3D shapes.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->The distance between surface and\n center of the sphere is called\n its radius.",bg="black",fg="white",width=60,font=15).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        Label(main,text="Surface Area of a Sphere",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text=" 4.π.radius*radius",bg="black",fg="white",width=60,font=15).pack()
        B1=Button(main,text="Find",command=Surface_Area_of_a_Sphere,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Volume of a Sphere",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text="4/3 π.radius*radius*radius",bg="black",fg="white",width=60,font=15).pack()
        
        B3=Button(main,text="Find",command=Volume_of_a_Sphere,bg="darkgreen",fg="White",font=15).pack()
        main.mainloop()
    def Hemisphere():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1400")
        main.title("HEMISPHERE")
        
        def Curved_Surface_Area_of_a_Hemisphere():
            def area():
                a1=int(R1.get())
                a=(2*(3.14)*(a1)*(a1))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60,font=15).pack()
            R1=Entry(main,bg="lightblue")
            R1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White",font=15).pack()
        def Total_Surface_Area_Hemisphere():
            def a1():
                a2=int(R2.get())
                a=(3*(3.14)*(a2)*(a2))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60,font=15).pack()
            R2=Entry(main,bg="lightblue")
            R2.pack()
            Button(main,text="Answer",command=a1,bg="darkgreen",fg="White",font=15).pack()
        def volume_of_a_Hemisphere():
            def v1():
                v3=int(v2.get())
                a=(2/3*(3.14)*(v3)*(v3)*(v3))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60,font=15).pack()
            v2=Entry(main,bg="lightblue")
            v2.pack()
            Button(main,text="Answer",command=v1,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Hemisphere",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
        
        Label(main,text=" What is a Hemisphere ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1400")
            main2.title("HEMISPHERE")
            Label(main2,text=" What is a Hemisphere ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
            Label(main2,text="->We can say, a hemisphere is \nexactly half of a sphere.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->A sphere makes exactly two\n hemispheres. One such good example of \n the hemisphere is our earth.\n Our earth consists of two hemispheres, \n namely Southern Hemisphere and the\n Northern Hemisphere.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->We can easily find the volume of\n the hemisphere \nsince the base of the sphere is \n circular. The volume of the hemisphere is\n derived by Archimedes.",bg="black",fg="white",width=60,font=15).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        Label(main,text="Curved Surface Area of Hemisphere",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text=" 2.π.radius*radius",bg="black",fg="white",width=60,font=15).pack()
        B1=Button(main,text="Find",command=Curved_Surface_Area_of_a_Hemisphere,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Total Surface Area  of Hemisphere",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text=" 3.π.radius*radius",bg="black",fg="white",width=60,font=15).pack()
        B2=Button(main,text="Find",command=Total_Surface_Area_Hemisphere,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Volume of a Hemisphere",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text="2/3 π.radius*radius*radius",bg="black",fg="white",width=60,font=15).pack()
        
        
        
        B3=Button(main,text="Volume",command=volume_of_a_Hemisphere,bg="darkgreen",fg="White",font=15).pack()
        main.mainloop()
    def Cylinder():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1400")
        main.title("CYLINDER")
        def Curved_Surface_Area_of_Cylinder():
            def area():
                a1=int(R1.get())
                a2=int(H1.get())
                a=(2*(3.14)*(a1)*(a2))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()         
            
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60,font=15).pack()
            R1=Entry(main,bg="lightblue")
            R1.pack()
            Label(main,text="Enter the height",bg="black",fg="yellow",width=60,font=15).pack()
            H1=Entry(main,bg="lightblue")
            H1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White",font=15).pack()
        def Total_Surface_Area_of_Cylinder():
            def a1():
                    a3=int(R2.get())
                    a4=int(H2.get())
                    a=(2*(3.14)*(a3)*(a3+a4))
                    ans=str(a)
                    Label(main,text="Your Area is "+ans,fg="white",bg="black",font="arial 15 bold ").pack()
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60,font=15).pack()
            R2=Entry(main,bg="lightblue")
            R2.pack()
            Label(main,text="Enter the height",bg="black",fg="yellow",width=60,font=15).pack()
            H2=Entry(main,bg="lightblue")
            H2.pack()
            Button(main,text="Answer",command=a1,bg="darkgreen",fg="White",font=15).pack()
        def Volume_of_Cylinder():
            def v1():
                a5=int(R3.get())
                a6=int(H3.get())
                a=((3.14)*(a5)*(a5)*(a6))
                ans=str(a)
                Label(main,text="Your  is Volume "+ans,fg="white",bg="black",font="arial 15 bold ").pack()
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60,font=15).pack()
            R3=Entry(main,bg="lightblue")
            R3.pack()
            Label(main,text="Enter the height",bg="black",fg="yellow",width=60,font=15).pack()
            H3=Entry(main,bg="lightblue")
            H3.pack()
            Button(main,text="Volume",command=v1,bg="darkgreen",fg="White").pack()
        Label(main,text="Cylinder",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
        
        Label(main,text=" What is a Cylinder ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1400")
            main2.title("CYLINDER")
            Label(main2,text=" What is a Cylinder ?",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
            Label(main2,text="->Cylinder is one of the basic 3d\n shapes, in geometry.",bg="black",fg="white",width=60,font=15).pack()
            Label(main2,text="->The perpendicular distance between\n the bases is the height, “h” and the distance \n  from the axis to the outer surface is the\n radius “r” of the cylinder.",bg="black",fg="white",width=60,font=15).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="arial 15 ").pack()
        Label(main,text="Surface Area of Cylinder",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text=" 2.π.radius.height",bg="black",fg="white",width=60,font=15).pack()
        B1=Button(main,text="Find",command=Curved_Surface_Area_of_Cylinder,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Total Surface Area of Cylinder",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text="2.π.radius(radius+height)",bg="black",fg="white",width=60,font=15).pack()
        B2=Button(main,text="Find",command=Total_Surface_Area_of_Cylinder,bg="darkgreen",fg="White",font=15).pack()
        Label(main,text="Volume of Cylinder",bg="black",fg="red",width=60,font=15).pack()
        Label(main,text=" π.radius*radius.height",bg="black",fg="white",width=60,font=15).pack()
        
        
        
        B3=Button(main,text="Find",command=Volume_of_Cylinder,bg="darkgreen",fg="White",font=15).pack()
        main.mainloop()
    """#Using Imgages
    CUBE=PhotoImage(file="CUBE B.png",width=200,height=200)
    
    CUBOID=PhotoImage(file="CUBOID B.png",width=200,height=200)
    CONE=PhotoImage(file="CONE B.png",width=200,height=200)
    CYLINDER=PhotoImage(file="CYLINDER B.png",width=200,height=200)
    SPHERE=PhotoImage(file="SPHERE B.png",width=200,height=200)
    HS=PhotoImage(file="HS.png",width=200,height=200)"""
    
    #Using Buttons
    Button(m,text="CUBE",command=Cube,bg="green",fg="white",width=20,font=15).pack()
    Button(m,text="CUBOID",command=Cuboid,bg="green",fg="white",width=20,font=15).pack()
    Button(m,text="SPHERE",command=Sphere,bg="green",fg="white",width=20,font=15).pack()
    Button(m,text="HEMISPHERE",command=Hemisphere,bg="green",fg="white",width=20,font=15).pack()
    Button(m,text="CYLINDER",command=Cylinder,bg="green",fg="white",width=20,font=15).pack()
    Button(m,text="TRIANGLE",command=Triangle,bg="green",fg="white",width=20,font=15).pack()
    Button(m,text="RECTANGULAR PRISM",command=Rectangular_Prism,bg="green",fg="white",width=20,font=15).pack()
    Button(m,text="CONE",command=Cone,bg="green",fg="white",width=20,font=15).pack()
    Button(m,text="RECTANGLE",command=Rectangle,bg="green",fg="white",width=20,font=15).pack()
    Button(m,text="SQUARE",command=Square,bg="green",fg="white",width=20,font=15).pack()
    
    
    #About us 
    mainframe=Frame(m,bg="black")
    mainframe.pack()
    Label(mainframe,text="About us",bg="black",fg="white",font="arial 15 underline").pack()
    Label(mainframe,text="Engineering Mathematics(4320002)",bg="black",fg="white",font="arial 14 italic").pack()
    Label(mainframe,text="Group No:-6",bg="black",fg="white",font="arial 14 italic").pack()
    Label(mainframe,text="216140316026  Miss.Sonali P Kale",bg="black",fg="white",font="arial 14 italic").pack()
    Label(mainframe,text="216140316027  Mr.Aryan K Patel",bg="black",fg="white",font="arial 14 italic").pack()
    Label(mainframe,text="2161403160214  Mr.Krish M Ujeniya",bg="black",fg="white",font="arial 14 italic").pack()
    Label(mainframe,text="216140316029  Miss.Mahek P Kahar",bg="black",fg="white",font="arial 14 italic").pack()
    Label(mainframe,text="216140316030  Mr.Harsh D Patel",bg="black",fg="white",font="arial 14 italic").pack()
    Label(mainframe,text="Guided by:-",bg="black",fg="white",font="arial 14 underline").pack()
    Label(mainframe,text="Miss.Asma H Rajwada",bg="black",fg="white",font="arial 14 italic").pack()
    Label(mainframe,text="Mr.Jayesh B Vasava",bg="black",fg="white",font="arial 14 italic").pack() 
    
    m.mainloop()
    

def mobile():
    m=Tk()
    m.config(bg="black")
    m.geometry("700x1200")
    m.title("Math Project For Mobile")
    Label(m,text="Surface Area & Volume",bg="black",fg="white",font="arial 15 bold underline").pack()
    def Triangle():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1200")
        main.title("TRIANGLE")
        def Area_of_a_Right_Angled_Triangle():
            def a1():
                a3=int(B2.get())
                a4=int(H2.get())
                a=(1/2*a3*a4)
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            Label(main,text="Enter the base",bg="black",fg="yellow",width=60).pack()
            B2=Entry(main,bg="lightblue")
            B2.pack()
            Label(main,text="Enter the height",bg="black",fg="yellow",width=60).pack()
            H2=Entry(main,bg="lightblue")
            H2.pack()
            Button(main,text="Answer",command=a1,bg="darkgreen",fg="White").pack()
        def Area_of_an_Equilateral_Triangle():
            def a2():
                a5=int(s2.get())
                a=((3**0.5/4)*(a5)*(a5))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            Label(main,text="Enter the side",bg="black",fg="yellow",width=60).pack()
            s2=Entry(main,bg="lightblue")
            s2.pack()
            Button(main,text="Answer",command=a2,bg="darkgreen",fg="White").pack()
        Label(main,text="Triangle",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
    
        Label(main,text=" What is a Triangle ?  ",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        def trians():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1200")
            main2.title("TRIANGLE")
            Label(main2,text=" What is a Triangle ?  ",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
            Label(main2,text="-> A triangle is a closed, 2-dimensional shape \nwith 3 sides, 3 angles, and 3 vertices.\n-> A triangle is also a polygon.Internal angle:\n 60° & Sum of interior angles: 180°\n We postulate the triangle principle which\n states that any information distance is\n well defined on any pair of measurements,\n even if the  two measurements cannot be jointly\n performed.\n-> As a consequence,  the triangle inequality for\n this distance is  obeyed for any\n three measurements.",bg="black",fg="white").pack()
            main2.mainloop()
        Button(main,text="Answer",command=trians,bg="darkgreen",fg="White").pack()
        
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        
        
        Label(main,text="Area of a Right Angled Triangle",bg="black",fg="red",width=60).pack()
        Label(main,text=" ½ × Base × Height ",bg="black",fg="white",width=60).pack()
        B2=Button(main,text="Find",command=Area_of_a_Right_Angled_Triangle,bg="darkgreen",fg="White").pack()
        Label(main,text="Area of an Equilateral Triangle",bg="black",fg="red",width=60).pack()
        Label(main,text=" (√3)/4 × side*side",bg="black",fg="white",width=60).pack()
        
        B3=Button(main,text="Find",command=Area_of_an_Equilateral_Triangle,bg="darkgreen",fg="White").pack()
        main.mainloop()
        
        
        
        
        
        
        
        
        
        
        
    def Rectangular_Prism():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1200")
        main.title("RECTANGULAR PRISM")
        def Surface_Area_of_a_Rectangular_Prism():
            def area():
                a1=int(R1.get())
                a2=int(W1.get())
                a=(2*(a1+a2))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            Label(main,text="Enter the Length",bg="black",fg="yellow",width=60).pack()
            R1=Entry(main,bg="lightblue")
            R1.pack()
            Label(main,text="Enter the Width ",bg="black",fg="yellow",width=60).pack()
            W1=Entry(main,bg="lightblue")
            W1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White").pack()
        def Total_Surface_Area_rectangular_prism():
            def a1():
                a3=int(L2.get())
                a4=int(W2.get())
                a5=int(H2.get())
                a=(2*(a3*a5)+(a4*a5)+(a3*a4))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            Label(main,text="Enter the Length ",bg="black",fg="yellow",width=60).pack()
            L2=Entry(main,bg="lightblue")
            L2.pack()
            Label(main,text="Enter the Width ",bg="black",fg="yellow",width=60).pack()
            W2=Entry(main,bg="lightblue")
            W2.pack()
            Label(main,text="Enter the Height",bg="black",fg="yellow",width=60).pack()
            H2=Entry(main,bg="lightblue")
            H2.pack()
            Button(main,text="Answer",command=a1,bg="darkgreen",fg="White").pack()
        def volume_of_a_rectangular_prism():
            def v1():
                v1=int(v4.get())
                v2=int(v5.get())
                v3=int(v6.get())
                a=(v1*v2*v3)
                ans=str(a)
                Label(main,text="Your Volume  is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            Label(main,text="Enter the Length",bg="black",fg="yellow",width=60).pack()
            v4=Entry(main,bg="lightblue")
            v4.pack()
            Label(main,text="Enter the Width ",bg="black",fg="yellow",width=60).pack()
            v5=Entry(main,bg="lightblue")
            v5.pack()
            Label(main,text="Enter the Height",bg="black",fg="yellow",width=60).pack()
            v6=Entry(main,bg="lightblue")
            v6.pack()
            Button(main,text="Answer",command=v1,bg="darkgreen",fg="White").pack()
        Label(main,text="Rectangular Prism",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
        
    
        Label(main,text=" What is a Rectangular Prism ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        def op():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1200")
            main2.title("RECTANGULAR PRISM")
            Label(main2,text=" What is a Rectangular Prism ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
            
            Label(main2,text="->In geometry, a rectangular prism is\n a polyhedron with two congruent \n and parallel bases. It is also called a cuboid.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->A rectangular prism is a three-\ndimensional shape, that has six faces \n (two at the top and bottom and four are\n lateral faces). All the faces of the prism \n  are rectangular in shape.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->A rectangular prism is a three-dimensional\n object. Hence, it will have its \n surface area and volume. To calculate the\n volume and surface area of a prism, \n we have to know the length of its sides or edges.\nLet ‘l’, ‘w’ and ‘h’ be the length, \n  width and height of the rectangular prism.",bg="black",fg="white",width=60).pack()
            main2.mainloop()
        Button(main,text="Answer",command=op,bg="darkgreen",fg="White").pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        Label(main,text="Surface Area of Rectangular Prism",bg="black",fg="red",width=60).pack()
        Label(main,text=" 2 (length + width)",bg="black",fg="white",width=60).pack()
        B1=Button(main,text="Find",command=Surface_Area_of_a_Rectangular_Prism,bg="darkgreen",fg="White").pack()
        Label(main,text="Total Surface Area  of Rectangular Prism",bg="black",fg="red",width=60).pack()
        Label(main,text=" 2 (length.height +width.height + length.width )",bg="black",fg="white",width=60).pack()
        B2=Button(main,text="Find",command=Total_Surface_Area_rectangular_prism,bg="darkgreen",fg="White").pack()
        Label(main,text="Volume of a Rectangular Prism",bg="black",fg="red",width=60).pack()
        Label(main,text="length*width*height",bg="black",fg="white",width=60).pack()
        
        
        
        B3=Button(main,text="Find",command=volume_of_a_rectangular_prism,bg="darkgreen",fg="White").pack()
        main.mainloop()
    def Cone():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1200")
        main.title("CONE")
        def Surface_Area_of_Cone():
            def area():
                a1=int(R1.get())
                a2=int(H1.get())
                l1=((a1)*(a1)+(a2)*(a2))
                l=(l1**0.5)
                a=((3.14)*(a1)*(a1+l))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60).pack()
            R1=Entry(main,bg="lightblue")
            R1.pack()
            Label(main,text="Enter the height",bg="black",fg="yellow",width=60).pack()
            H1=Entry(main,bg="lightblue")
            H1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White").pack()
        def Volume_of_Cone():
            def v1():
                a3=int(R2.get())
                a4=int(H2.get())
                a=(1/3*(3.14)*(a3)*(a3)*(a4))
                ans=str(a)
                Label(main,text="Your Volume is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60).pack()
            R2=Entry(main,bg="lightblue")
            R2.pack()
            Label(main,text="Enter the height",bg="black",fg="yellow",width=60).pack()
            H2=Entry(main,bg="lightblue")
            H2.pack()
            Button(main,text="Answer",command=v1,bg="darkgreen",fg="White").pack()
        Label(main,text="Cone.",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
    
        Label(main,text=" What is a Cone ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        def mar():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1200")
            main2.title("CONE")
            Label(main2,text=" What is a Cone ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
            Label(main2,text="->A cone is a three-dimensional shape\n in geometry that narrows smoothly \n from a flat base (usually circular base) to a\n point(which forms an axis to the \n centre of base) called the apex or vertex.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->These cones are also stated \nas a circular cone.",bg="black",fg="white",width=60).pack()
            main2.mainloop()
        Button(main,text="Answer",command=mar,bg="darkgreen",fg="White").pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        Label(main,text="Surface Area of the Cone",bg="black",fg="red",width=60).pack()
        Label(main,text=" π.radius(length + radius)",bg="black",fg="white",width=60).pack()
        B1=Button(main,text="Find",command=Surface_Area_of_Cone,bg="darkgreen",fg="White").pack()
        
        Label(main,text="Volume of the Cone",bg="black",fg="red",width=60).pack()
        Label(main,text="  ⅓ π.radius*radius.height",bg="black",fg="white",width=60).pack()
    
        
        B2=Button(main,text="Find",command=Volume_of_Cone,bg="darkgreen",fg="White").pack()
        main.mainloop()
    def Rectangle():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1200")
        main.title("RECTANGLE")
        def Area_of_Rectangle():
            def area():
                a1=int(L1.get())
                a2=int(W1.get())
                a=((a1)*(a2))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            
            Label(main,text="Enter the Length",bg="black",fg="yellow",width=60).pack()
            L1=Entry(main,bg="lightblue")
            L1.pack()
            Label(main,text="Enter the Width",bg="black",fg="yellow",width=60).pack()
            W1=Entry(main,bg="lightblue")
            W1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White").pack()
        Label(main,text="Rectangle",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
    
        Label(main,text=" What is a Rectangle ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1200")
            main2.title("RECTANGLE")
            Label(main2,text=" What is a Rectangle ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
            Label(main2,text="->A Rectangle is a four sided-polygon,\n having all the internal angles equal \n to 90 degrees. ",bg="black",fg="white",width=60).pack()
            Label(main2,text="->A rectangle is characterized by length (L)\n and width (W). Both length \n and width are different in size.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->Sum of all interior angles equal to 360 degrees.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->The opposite sides are equal and parallel.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->It’s a parallelogram with four right angles.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->Area is equal to product of its length\n and breadth.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->It has four sides and four vertices.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->The most common everyday things or\n objects we see and are rectangular \n in shape is Television, computer screen,\n notebook, mobile phones, CPU , \n Notice boards,Table, Book, TV screen,\n Mobile phone, Wall, Magazine, \n Tennis court, etc.",bg="black",fg="white",width=60).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White").pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        Label(main,text="Area of Rectangle",bg="black",fg="red",width=60).pack()
        Label(main,text="length*width",bg="black",fg="white",width=60).pack()
        
        B1=Button(main,text="Find",command=Area_of_Rectangle,bg="darkgreen",fg="White").pack()
        main.mainloop()
    def Square():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1200")
        main.title("SQUARE")
        def Area_of_Square():
            def area():
                a1=int(L1.get())
                a=((a1)*(a1))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            
            Label(main,text="Enter the Side",bg="black",fg="yellow",width=60).pack()
            L1=Entry(main,bg="lightblue")
            L1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White").pack()
        Label(main,text="Square",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
    
        Label(main,text=" What is a Square ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1200")
            main2.title("RECTANGLE")
        
            Label(main2,text=" What is a Square ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
            Label(main2,text="->Square is a regular quadrilateral",bg="black",fg="white",width=60).pack()
            Label(main2,text="->a square where all the sides are\n equal and each angle equals 90 degrees.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->The length of diagonals is greater\n than the sides of the square.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->The diagonals of the square\n bisect each other at 90°.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->All four sides of the square are congruent\n or equal to each other.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->The diagonal of the square divide it\n into two similar isosceles triangles.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->There are many examples of square shape\n in real-life such as a square plot \n or field, a square-shaped ground, square\n-shaped table cloth, the tiles of \n the floor in square shape, etc.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->A square is a four-sided polygon, whose\n all its sides are equal in length and \n opposite sides are parallel  to each other.\n Also, each vertices of square \n have angle equal to 90 degrees.",bg="black",fg="white",width=60).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White").pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        Label(main,text="Area of square",bg="black",fg="red",width=60).pack()
        Label(main,text="side*side",bg="black",fg="white",width=60).pack()
        
        B1=Button(main,text="Find",command=Area_of_Square,bg="darkgreen",fg="White").pack()
        main.mainloop()
    def Cuboid():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1200")
        main.title("CUBOID")
        def Cuboid_Area():
            def area():
                a1=int(L1.get())
                a2=int(B1.get())
                a3=int(H1.get())
                a=(2*a3)*(a1+a2)
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            
            Label(main,text="Enter the Length",bg="black",fg="yellow",width=60).pack()
            L1=Entry(main,bg="lightblue")
            L1.pack()
            Label(main,text="Enter the breath",bg="black",fg="yellow",width=60).pack()
            B1=Entry(main,bg="lightblue")
            B1.pack()
            Label(main,text="Enter the Height",bg="black",fg="yellow",width=60).pack()
            H1=Entry(main,bg="lightblue")
            H1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White").pack()
        def Cuboid_T_Area():
            def a2():
                a1=int(L1.get())
                a2=int(B1.get())
                a3=int(H1.get())
                a=2*((a1*a2)+(a2*a3)+(a1*a3))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()               
            Label(main,text="Enter the Length",bg="black",fg="yellow",width=60).pack()
            L1=Entry(main,bg="lightblue")
            L1.pack()
            Label(main,text="Enter the breath",bg="black",fg="yellow",width=60).pack()
            B1=Entry(main,bg="lightblue")
            B1.pack()
            Label(main,text="Enter the Height",bg="black",fg="yellow",width=60).pack()
            H1=Entry(main,bg="lightblue")
            H1.pack()
            Button(main,text="Answer",command=a2,bg="darkgreen",fg="White").pack()
    
        Label(main,text="Cuboid",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
        Label(main,text=" What is a Cuboid ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        
        
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1200")
            main2.title("CUBOID")
            Label(main2,text=" What is a Cuboid ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
            Label(main2,text="->A cuboid is a three dimensional\n solid that has 6 faces (rectangular), \n  8 vertices and 12 edges. A cuboid has\n three dimensions such as length, width \n and height. A perfect  cuboid is said\n to be a cuboid that has integer edges.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->Cuboid has three dimensions:\n length, width and height.",bg="black",fg="white",width=60).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White").pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        Label(main,text="Cuboid Lateral Surface Area",bg="black",fg="red",width=60).pack()
        Label(main,text="2.height(length + width)",bg="black",fg="white",width=60).pack()
        B1=Button(main,text="Find",command=Cuboid_Area,bg="darkgreen",fg="White").pack()
        Label(main,text="Cuboid Total Surface Area.",bg="black",fg="red",width=60).pack()
        Label(main,text="2.(length.width + width.height + height.length)",bg="black",fg="white",width=60).pack()
      
        
        B2=Button(main,text="Find",command=Cuboid_T_Area,bg="darkgreen",fg="White").pack()
        main.mainloop()
    def Cube():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1200")
        main.title("CUBE")
        def Area_of_one_face_cube():
            def area():
                a1=int(L1.get())
                a=((a1)*(a1))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()       
            Label(main,text="Enter the Side",bg="black",fg="yellow",width=60).pack()
            L1=Entry(main,bg="lightblue")
            L1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White").pack()
        def Lateral_surface_area_cube():
            def a2():
                a1=int(L2.get())
                a=(4*(a1)*(a1))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()               
            Label(main,text="Enter the side",bg="black",fg="yellow",width=60).pack()
            L2=Entry(main,bg="lightblue")
            L2.pack()
            Button(main,text="Answer",command=a2,bg="darkgreen",fg="White").pack()
    
        Label(main,text="Cube",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
        
        Label(main,text=" What is a Cube ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1200")
            main2.title("CUBE")
            Label(main2,text=" What is a Cube ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
            Label(main2,text="->As discussed earlier,\n a cube is a 3-D.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->solid shape, which has 6 faces.\n A cube is one of the simplest shapes in three \n dimensional space. All the six faces of \na cube are squares, a twodimensional  \n shape.",bg="black",fg="white",width=60).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White").pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        Label(main,text="One face Area",bg="black",fg="red",width=60).pack()
        Label(main,text=" side*side",bg="black",fg="white",width=60).pack()
        B1=Button(main,text="Find",command=Area_of_one_face_cube,bg="darkgreen",fg="White").pack()
        Label(main,text="Lateral surface of Cube",bg="black",fg="red",width=60).pack()
        Label(main,text="4*side*side",bg="black",fg="white",width=60).pack()
    
        
        B2=Button(main,text="Find",command=Lateral_surface_area_cube,bg="darkgreen",fg="White").pack()
        main.mainloop()
    def Sphere():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1200")
        main.title("SPHERE")
        def Surface_Area_of_a_Sphere():
            def area():
                a1=int(R1.get())
                a=(4*(3.14)*(a1)*(a1))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60).pack()
            R1=Entry(main,bg="lightblue")
            R1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White").pack()
        def Volume_of_a_Sphere():
            def a1():
                    a2=int(R2.get())
                    a=(4/3*(3.14)*(a2)*(a2)*(a2))
                    ans=str(a)
                    Label(main,text="Your Volume is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60).pack()
            R2=Entry(main,bg="lightblue")
            R2.pack()
            Button(main,text="Answer",command=a1,bg="darkgreen",fg="White").pack()
        Label(main,text="Sphere",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
        
        Label(main,text=" What is a Sphere ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1200")
            main2.title("SPHERE")
            Label(main2,text=" What is a Sphere ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
            Label(main2,text="->A sphere is a three-dimensional\n object that is round in shape.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->A sphere does not have any edges\n or vertices, like other 3D shapes.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->The distance between surface and\n center of the sphere is called\n its radius.",bg="black",fg="white",width=60).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White").pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        Label(main,text="Surface Area of a Sphere",bg="black",fg="red",width=60).pack()
        Label(main,text=" 4.π.radius*radius",bg="black",fg="white",width=60).pack()
        B1=Button(main,text="Find",command=Surface_Area_of_a_Sphere,bg="darkgreen",fg="White").pack()
        Label(main,text="Volume of a Sphere",bg="black",fg="red",width=60).pack()
        Label(main,text="4/3 π.radius*radius*radius",bg="black",fg="white",width=60).pack()
        
        B3=Button(main,text="Find",command=Volume_of_a_Sphere,bg="darkgreen",fg="White").pack()
        main.mainloop()
    def Hemisphere():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1200")
        main.title("HEMISPHERE")
        
        def Curved_Surface_Area_of_a_Hemisphere():
            def area():
                a1=int(R1.get())
                a=(2*(3.14)*(a1)*(a1))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60).pack()
            R1=Entry(main,bg="lightblue")
            R1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White").pack()
        def Total_Surface_Area_Hemisphere():
            def a1():
                a2=int(R2.get())
                a=(3*(3.14)*(a2)*(a2))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            Label(main,text="Enter the radius",bg="black",fg="yellow").pack()
            R2=Entry(main,bg="lightblue")
            R2.pack()
            Button(main,text="Answer",command=a1,bg="darkgreen",fg="White").pack()
        def volume_of_a_Hemisphere():
            def v1():
                v3=int(v2.get())
                a=(2/3*(3.14)*(v3)*(v3)*(v3))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60).pack()
            v2=Entry(main,bg="lightblue")
            v2.pack()
            Button(main,text="Answer",command=v1,bg="darkgreen",fg="White").pack()
        Label(main,text="Hemisphere",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
        
        Label(main,text=" What is a Hemisphere ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1200")
            main2.title("HEMISPHERE")
            Label(main2,text=" What is a Hemisphere ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
            Label(main2,text="->We can say, a hemisphere is \nexactly half of a sphere.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->A sphere makes exactly two\n hemispheres. One such good example of \n the hemisphere is our earth.\n Our earth consists of two hemispheres, \n namely Southern Hemisphere and the\n Northern Hemisphere.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->We can easily find the volume of\n the hemisphere \nsince the base of the sphere is \n circular. The volume of the hemisphere is\n derived by Archimedes.",bg="black",fg="white",width=60).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White").pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        Label(main,text="Curved Surface Area of Hemisphere",bg="black",fg="red",width=60).pack()
        Label(main,text=" 2.π.radius*radius",bg="black",fg="white",width=60).pack()
        B1=Button(main,text="Find",command=Curved_Surface_Area_of_a_Hemisphere,bg="darkgreen",fg="White").pack()
        Label(main,text="Total Surface Area  of Hemisphere",bg="black",fg="red",width=60).pack()
        Label(main,text=" 3.π.radius*radius",bg="black",fg="white",width=60).pack()
        B2=Button(main,text="Find",command=Total_Surface_Area_Hemisphere,bg="darkgreen",fg="White").pack()
        Label(main,text="Volume of a Hemisphere",bg="black",fg="red",width=60).pack()
        Label(main,text="2/3 π.radius*radius*radius",bg="black",fg="white",width=60).pack()
        
        
        
        B3=Button(main,text="Volume",command=volume_of_a_Hemisphere,bg="darkgreen",fg="White").pack()
        main.mainloop()
    def Cylinder():
        main=Tk()
        main.config(bg="black")
        main.geometry("700x1200")
        main.title("CYLINDER")
        def Curved_Surface_Area_of_Cylinder():
            def area():
                a1=int(R1.get())
                a2=int(H1.get())
                a=(2*(3.14)*(a1)*(a2))
                ans=str(a)
                Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()         
            
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60).pack()
            R1=Entry(main,bg="lightblue")
            R1.pack()
            Label(main,text="Enter the height",bg="black",fg="yellow",width=60).pack()
            H1=Entry(main,bg="lightblue")
            H1.pack()
            Button(main,text="Answer",command=area,bg="darkgreen",fg="White").pack()
        def Total_Surface_Area_of_Cylinder():
            def a1():
                    a3=int(R2.get())
                    a4=int(H2.get())
                    a=(2*(3.14)*(a3)*(a3+a4))
                    ans=str(a)
                    Label(main,text="Your Area is "+ans,fg="white",bg="black",font="roman 10 bold ").pack()
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60).pack()
            R2=Entry(main,bg="lightblue")
            R2.pack()
            Label(main,text="Enter the height",bg="black",fg="yellow",width=60).pack()
            H2=Entry(main,bg="lightblue")
            H2.pack()
            Button(main,text="Answer",command=a1,bg="darkgreen",fg="White").pack()
        def Volume_of_Cylinder():
            def v1():
                a5=int(R3.get())
                a6=int(H3.get())
                a=((3.14)*(a5)*(a5)*(a6))
                ans=str(a)
                Label(main,text="Your  is Volume "+ans,fg="white",bg="black",font="roman 10 bold ").pack()
            Label(main,text="Enter the radius",bg="black",fg="yellow",width=60).pack()
            R3=Entry(main,bg="lightblue")
            R3.pack()
            Label(main,text="Enter the height",bg="black",fg="yellow",width=60).pack()
            H3=Entry(main,bg="lightblue")
            H3.pack()
            Button(main,text="Volume",command=v1,bg="darkgreen",fg="White").pack()
        Label(main,text="Cylinder",bg="black",fg="white",font="arial 15 bold underline",width=60).pack()
        
        Label(main,text=" What is a Cylinder ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        def b():
            main2=Tk()
            main2.config(bg="black")
            main2.geometry("700x1200")
            main2.title("CYLINDER")
            Label(main2,text=" What is a Cylinder ?",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
            Label(main2,text="->Cylinder is one of the basic 3d\n shapes, in geometry.",bg="black",fg="white",width=60).pack()
            Label(main2,text="->The perpendicular distance between\n the bases is the height, “h” and the distance \n  from the axis to the outer surface is the\n radius “r” of the cylinder.",bg="black",fg="white",width=60).pack()
            main2.mainloop()
        Button(main,text="Answer",command=b,bg="darkgreen",fg="White").pack()
        Label(main,text="Formulas",bg="black",fg="yellow",width=60,font="roman 10 ").pack()
        Label(main,text="Surface Area of Cylinder",bg="black",fg="red",width=60).pack()
        Label(main,text=" 2.π.radius.height",bg="black",fg="white",width=60).pack()
        B1=Button(main,text="Find",command=Curved_Surface_Area_of_Cylinder,bg="darkgreen",fg="White").pack()
        Label(main,text="Total Surface Area of Cylinder",bg="black",fg="red",width=60).pack()
        Label(main,text="2.π.radius(radius+height)",bg="black",fg="white",width=60).pack()
        B2=Button(main,text="Find",command=Total_Surface_Area_of_Cylinder,bg="darkgreen",fg="White").pack()
        Label(main,text="Volume of Cylinder",bg="black",fg="red",width=60).pack()
        Label(main,text=" π.radius*radius.height",bg="black",fg="white",width=60).pack()
        
        
        
        B3=Button(main,text="Find",command=Volume_of_Cylinder,bg="darkgreen",fg="White").pack()
        main.mainloop()
    """#Using Imgages
    CUBE=PhotoImage(file="CUBE B.png",width=200,height=200)
    
    CUBOID=PhotoImage(file="CUBOID B.png",width=200,height=200)
    CONE=PhotoImage(file="CONE B.png",width=200,height=200)
    CYLINDER=PhotoImage(file="CYLINDER B.png",width=200,height=200)
    SPHERE=PhotoImage(file="SPHERE B.png",width=200,height=200)
    HS=PhotoImage(file="HS.png",width=200,height=200)"""
    
    #Using Buttons
    Button(m,text="CUBE",command=Cube,bg="green",fg="white",width=20).pack()
    Button(m,text="CUBOID",command=Cuboid,bg="green",fg="white",width=20).pack()
    Button(m,text="SPHERE",command=Sphere,bg="green",fg="white",width=20).pack()
    Button(m,text="HEMISPHERE",command=Hemisphere,bg="green",fg="white",width=20).pack()
    Button(m,text="CYLINDER",command=Cylinder,bg="green",fg="white",width=20).pack()
    Button(m,text="TRIANGLE",command=Triangle,bg="green",fg="white",width=20).pack()
    Button(m,text="RECTANGULAR PRISM",command=Rectangular_Prism,bg="green",fg="white",width=20).pack()
    Button(m,text="CONE",command=Cone,bg="green",fg="white",width=20).pack()
    Button(m,text="RECTANGLE",command=Rectangle,bg="green",fg="white",width=20).pack()
    Button(m,text="SQUARE",command=Square,bg="green",fg="white",width=20).pack()
    
    
    #About us 
    mainframe=Frame(m,bg="black")
    mainframe.pack()
    Label(mainframe,text="About us",bg="black",fg="white",font="arial 10 underline").pack()
    Label(mainframe,text="Engineering Mathematics(4320002)",bg="black",fg="white",font="arial 8 italic").pack()
    Label(mainframe,text="Group No:-6",bg="black",fg="white",font="arial 8 italic").pack()
    Label(mainframe,text="216120316026  Miss.Sonali P Kale",bg="black",fg="white",font="arial 8 italic").pack()
    Label(mainframe,text="216120316027  Mr.Aryan K Patel",bg="black",fg="white",font="arial 8 italic").pack()
    Label(mainframe,text="216120316028  Mr.Krish M Ujeniya",bg="black",fg="white",font="arial 8 italic").pack()
    Label(mainframe,text="216120316029  Miss.Mahek P Kahar",bg="black",fg="white",font="arial 8 italic").pack()
    Label(mainframe,text="216120316030  Mr.Harsh D Patel",bg="black",fg="white",font="arial 8 italic").pack()
    Label(mainframe,text="Guided by:-",bg="black",fg="white",font="arial 8 underline").pack()
    Label(mainframe,text="Miss.Asma H Rajwada",bg="black",fg="white",font="arial 8 italic").pack()
    Label(mainframe,text="Mr.Jayesh B Vasava",bg="black",fg="white",font="arial 8 italic").pack() 
    
    m.mainloop()
Button(Math,text='For\n Mobile',command=mobile,fg="light green",bg="black",font="arial 30 bold",width=9).pack()  
Label(Math,text="\n\n\n",bg="black").pack()
Button(Math,text='For\n Laptop',command=Laptop,fg="light green",bg="black",font="arial 30 bold",width=9).pack()  
Math.mainloop()