print("WELCOME TO ABC HOSPITALS PVT.LTD")
import datetime
now=datetime.datetime.now()
print("Current date and time is: ")
print(now.strftime("%y-%m-%d %H:%M:%S"))



print("1.LOGIN")
print("2.REGISTER")


r=int(input("enter your choice:"))

if r==2:
    import mysql.connector
    mydb=mysql.connector.connect(host="Localhost",user="root",passwd="Bhulgya247",database="project" , auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    print("|||| PLEASE REGISTER YOURSELF||||")
    u=input("ENTER YOUR USERNAME:")
    p=input("ENTER YOUR PASSWORD (PASSWORD SHOULD BE STRONG:)")
    mycursor.execute("insert into user values('"+str(u)+"','"+str(p)+"')")
    mydb.commit()
    print(" |||| REGISTERED SUCCESSFULLY||||")

elif r==1:
    print("!!!! {LOGIN}!!!!")
    
    un=input("ENTER THE USERNAME:")
    ps=input("ENTER THE PASSWORD:")
   
    import mysql.connector
    mydb=mysql.connector.connect(host="Localhost",user="root",passwd="Bhulgya247",database="project" , auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    mycursor.execute("select password from user where username='"+str(un)+"'")
   
    row=mycursor.fetchall()
    for x in row:
        a=list(x)
        if a[0]==str(ps):
                  
            
                c='y'
                while(c=='y'):
            
                    print("1.ADMINISTRATION")
                    print("2.BILLING")
                    print("3.APPOINTMENT")
                    print("4.SIGNOUT")
                    a=int(input("ENTER YOUR CHOICE:"))
          
                    if a==1:
                       print("1.SHOW DETAILS") 
                       print("2.ADD NEW MEMBER")
                       print("3.DELETE EXISTING ONE") 
                       print("4.EXIT")
                         
                       b=int(input("ENTER YOUR CHOICE:"))
            
                       if b==1:
                           print("1.DOCTOR DETAILS:")
                           print("2.PATIENT DETAILS:")
                                       
                           c=int(input("enter your choice:"))
                           if c==1:
                              import mysql.connector
                              mydb=mysql.connector.connect(host="Localhost",user="root",passwd="Bhulgya247",database="project" , auth_plugin='mysql_native_password')
                              mycursor=mydb.cursor()
                              mycursor.execute("select drname,specialisation,experienced from doctor")
                              row=mycursor.fetchall()
                              print(row)
                              
                           elif c==2:
                               import mysql.connector
                               mydb=mysql.connector.connect(host="Localhost",user="root",passwd="Bhulgya247",database="project" , auth_plugin='mysql_native_password')
                               mycursor=mydb.cursor()
                               mycursor.execute("select * from patient")
                               myrecords=mycursor.fetchall()
                               for x in myrecords:
                                   print(x)
                       
                        
                       elif b==2:
                           print("1.DOCTOR DETAILS:")
                           print("2.patient DETAILS:")
                           c1=int(input("enter your choice"))
                           
                           
                           if c1==1:
                               import mysql.connector
                               mydb=mysql.connector.connect(host="Localhost",user="root",passwd="Bhulgya247",database="project" , auth_plugin='mysql_native_password')
                               mycursor=mydb.cursor()
                               doctorid=input("ENTER THE DR.ID:")
                               drname=input("ENTER THE DR.NAME:")
                               specialisation=input("ENTER YOUR SPECIALISATION:")
                               experienced=int(input("ENTER YOUR EXPERIENCED:"))
                               doctorsfee=int(input("ENTER DOCTOR'S FEE:"))
                               opd=input("ENTER OPD:")
                               mycursor.execute("insert into doctor values('"+doctorid+"','"+drname+"','"+specialisation+"','"+str(experienced)+"','"+str(doctorsfee)+"','"+opd+"')")
                               mydb.commit()
                               print("SUCCESSFULLY ADDED")
                               
                           elif c1==2:
                               import mysql.connector
                               mydb=mysql.connector.connect(host="Localhost",user="root",passwd="Bhulgya247",database="project" , auth_plugin='mysql_native_password')
                               mycursor=mydb.cursor()
                               pname=input("ENTER THE NAME:")
                               bloodgroup=input("ENTER YOUR BLOODGRP:")
                               gender=input("ENTER THE GENDER:")
                               dob=input("ENTER DATE OF BIRTH:")
                               opd=input("ENTER THE OPD:")
                               patienthistory=input("ENTER THE PATIENT HISTORY:")
                               roomno=input("ENTER THE ROOM NO:")
                               mycursor.execute("insert into patient values('"+pname+"','"+bloodgroup+"','"+gender+"','"+dob+"','"+opd+"','"+patienthistory+"','"+str(roomno)+"')")
                               mydb.commit()
                               print("SUCCESSFULLY ADDED")

                       elif b==3:
                            print("1.DOCTOR DETAILS:")
                            print("2.PATIENT DETAILS:")
                            c2=int(input("enter your choice"))
                            if c2==1:
                                import mysql.connector
                                mydb=mysql.connector.connect(host="Localhost",user="root",passwd="Bhulgya247",database="project" , auth_plugin='mysql_native_password')
                                mycursor=mydb.cursor()
                                drname=input("ENTER DOCTOR'S NAME:")
                                mycursor.execute("select * from doctor where drname='"+drname+"'")
                                row=mycursor.fetchall()
                                print(row)
                                p=input("you really wanna delete this data? (y/n):")
                                if p=="y":
                                    mycursor.execute("delete from doctor where drname='"+drname+"'")
                                    mydb.commit()
                                    print("SUCCESSFULLY DELETED!!")
                                else:
                                    print("NOT DELETED")
                            elif c2==2:
                                import mysql.connector
                                mydb=mysql.connector.connect(host="Localhost",user="root",passwd="Bhulgya247",database="project" , auth_plugin='mysql_native_password')
                                mycursor=mydb.cursor()
                                pname=input("ENTER PATIENT'S NAME:")
                                mycursor.execute("select * from patient where pname='"+pname+"'")
                                row=mycursor.fetchall()
                                print(row)
                                p=input("you really wanna delete this data? (y/n):")
                                if p=="y":
                                    mycursor.execute("delete from patient where pname='"+pname+"'")
                                    mydb.commit()
                                    print("SUCCESSFULLY DELETED!!")
                                else:
                                    print("NOT DELETED" )
                       elif b==4:
                          break
                      
                        
                    elif a==2:
                        import mysql.connector
                        mydb=mysql.connector.connect(host="Localhost",user="root",passwd="Bhulgya247",database="project" , auth_plugin='mysql_native_password')
                        mycursor=mydb.cursor()
                        opd=input("ENTER THE OPD:")
                        
                        mycursor.execute("select drname,specialisation,doctorsfee,pname,patienthistory,roomtype,roomcharges from doctor d inner join patient p on d.opd=p.opd inner join room r on p.roomno=r.roomno where p.opd='"+opd+"'")
                        for x in mycursor:
                            print(x)
                            bill=input("HAS HE PAID ALL THE BILLS ? (y/n):")
                            if bill=="y":
                                mycursor.execute("delete from patient where opd='"+opd+"'")
                                mydb.commit()
                                print("billing is successfull")
                            else:
                                print("not paid!!!!!")
                    elif a==3:
                        print("TO BOOK AN APPOINTMENT ENTER 1:")
                        print("TO EDIT AN APPOINTMENT ENTER 2:")
                        print("TO CANCEL AN APPOINTMENT ENTER 3:")
                        print("TO BE BACK ENTER 4:")
                        c3=int(input("YOUR CHOICE:"))
                        if c3==1:
                            import mysql.connector
                            mydb=mysql.connector.connect(host="Localhost",user="root",passwd="Bhulgya247",database="project" , auth_plugin='mysql_native_password')
                            mycursor=mydb.cursor()  
                            doctorid=input("ENTER THE DR.ID:")
                            opd=input("ENTER patient id:")
                            sessionst=input("SESSION STARTS AT :")
                            sessionends=input("SESSION ENDS AT:")
                            gender=input("ENTER THE GENDER:")
                            mycursor.execute("insert into appointment values('"+doctorid+"','"+opd+"','"+sessionst+"','"+sessionends+"','"+gender+"')")
                            mydb.commit()
                            print("SUCCESSFULLY ADDED")
                            
                            
                        elif c3==2:
                            import mysql.connector
                            mydb=mysql.connector.connect(host="Localhost",user="root",passwd="Bhulgya247",database="project" , auth_plugin='mysql_native_password')
                            mycursor=mydb.cursor()  
                            opd=input("enter patientid:")
                            mycursor.execute("update appointment set sessionst=sessionst+.30 where opd='"+opd+"'")
                            mycursor.execute("update appointment set sessionends=sessionends+.30 where opd='"+opd+"'")
                            mydb.commit()
                            print("SUCCESSFULLY UPDATED:")
                            
                            
                        elif c3==3:
                            import mysql.connector
                            mydb=mysql.connector.connect(host="Localhost",user="root",passwd="Bhulgya247",database="project" , auth_plugin='mysql_native_password')
                            mycursor=mydb.cursor()  
                            opd=input("ENTER patient id:")
                            mycursor.execute("select * from appointment where opd='"+opd+"'")
                            row=mycursor.fetchall()
                            print(row)
                            p=input("you really wanna delete this data? (y/n):")
                            if p=="y":
                                mycursor.execute("delete from appointment where opd='"+opd+"'")
                                mydb.commit()
                                print("SUCCESSFULLY DELETED!!")
                            else:
                               print("NOT DELETED")
                        elif c3==4:
                            break
                    
                    else:
                        break










