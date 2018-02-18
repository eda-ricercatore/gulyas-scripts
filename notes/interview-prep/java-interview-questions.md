hat if the main method is declared as private?

The program compiles properly but at runtime it will give “Main method not public.” message.

What is meant by pass by reference and pass by value in Java?

Pass by reference means, passing the address itself rather than passing the value. Pass by value means passing a copy of the value.

If you’re overriding the method equals() of an object, which other method you might also consider?

hashCode()

What is Byte Code?

Or

What gives java it’s “write once and run anywhere” nature?

All Java programs are compiled into class files that contain bytecodes. These byte codes can be run in any platform and hence java is said to be platform independent.

Expain the reason for each keyword of public static void main(String args[])?

public- main(..) is the first method called by java environment when a program is executed so it has to accessible from java environment. Hence the access specifier has to be public.

static: Java environment should be able to call this method without creating an instance of the class , so this method must be declared as static.

void: main does not return anything so the return type must be void

The argument String indicates the argument type which is given at the command line and arg is an array for string given during command line.

What are the differences between == and .equals() ?

Or

what is difference between == and equals

Or

Difference between == and equals method

Or

What would you use to compare two String variables - the operator == or the method equals()?

Or

How is it possible for two String objects with identical values not to be equal under the == operator?

The == operator compares two objects to determine if they are the same object in memory i.e. present in the same memory location. It is possible for two String objects to have the same value, but located in different areas of memory.

== compares references while .equals compares contents. The method public boolean equals(Object obj) is provided by the Object class and can be overridden. The default implementation returns true only if the object is compared with itself, which is equivalent to the equality operator == being used to compare aliases to the object. String, BitSet, Date, and File override the equals() method. For two String objects, value equality means that they contain the same character sequence. For the Wrapper classes, value equality means that the primitive values are equal.

 public class EqualsTest {

	public static void main(String[] args) {

		String s1 = “abc”;
		String s2 = s1;
		String s5 = “abc”;
		String s3 = new String(”abc”);
		String s4 = new String(”abc”);
		System.out.println(”== comparison : ” + (s1 == s5));
		System.out.println(”== comparison : ” + (s1 == s2));
		System.out.println(”Using equals method : ” + s1.equals(s2));
		System.out.println(”== comparison : ” + s3 == s4);
		System.out.println(”Using equals method : ” + s3.equals(s4));
	}
}

Output
== comparison : true
== comparison : true
Using equals method : true
false
Using equals method : true

What if the static modifier is removed from the signature of the main method?

Or

What if I do not provide the String array as the argument to the method?

Program compiles. But at runtime throws an error “NoSuchMethodError”.

Why oracle Type 4 driver is named as oracle thin driver?

Oracle provides a Type 4 JDBC driver, referred to as the Oracle “thin” driver. This driver includes its own implementation of a TCP/IP version of Oracle’s Net8 written entirely in Java, so it is platform independent, can be downloaded to a browser at runtime, and does not require any Oracle software on the client side. This driver requires a TCP/IP listener on the server side, and the client connection string uses the TCP/IP port address, not the TNSNAMES entry for the database name.

What is the difference between final, finally and finalize? What do you understand by the java final keyword?

Or

What is final, finalize() and finally?

Or

What is finalize() method?

Or

What is the difference between final, finally and finalize?

Or

What does it mean that a class or member is final?

o final - declare constant
o finally - handles exception
o finalize - helps in garbage collection

Variables defined in an interface are implicitly final. A final class can’t be extended i.e., final class may not be subclassed. This is done for security reasons with basic classes like String and Integer. It also allows the compiler to make some optimizations, and makes thread safety a little easier to achieve. A final method can’t be overridden when its class is inherited. You can’t change value of a final variable (is a constant). finalize() method is used just before an object is destroyed and garbage collected. finally, a key word used in exception handling and will be executed whether or not an exception is thrown. For example, closing of open connections is done in the finally method.

What is the Java API?

The Java API is a large collection of ready-made software components that provide many useful capabilities, such as graphical user interface (GUI) widgets.

What is the GregorianCalendar class?

The GregorianCalendar provides support for traditional Western calendars.

What is the ResourceBundle class?

The ResourceBundle class is used to store locale-specific resources that can be loaded by a program to tailor the program’s appearance to the particular locale in which it is being run.

Why there are no global variables in Java?

Global variables are globally accessible. Java does not support globally accessible variables due to following reasons:

    * The global variables breaks the referential transparency
    * Global variables creates collisions in namespace.

How to convert String to Number in java program?

The valueOf() function of Integer class is is used to convert string to Number. Here is the code example:
String numString = “1000″;
int id=Integer.valueOf(numString).intValue();

What is the SimpleTimeZone class?

The SimpleTimeZone class provides support for a Gregorian calendar.

What is the difference between a while statement and a do statement?

A while statement (pre test) checks at the beginning of a loop to see whether the next loop iteration should occur. A do while statement (post test) checks at the end of a loop to see whether the next iteration of a loop should occur. The do statement will always execute the loop body at least once.

What is the Locale class?

The Locale class is used to tailor a program output to the conventions of a particular geographic, political, or cultural region.

Describe the principles of OOPS.

There are three main principals of oops which are called Polymorphism, Inheritance and Encapsulation.

Explain the Inheritance principle.

Inheritance is the process by which one object acquires the properties of another object. Inheritance allows well-tested procedures to be reused and enables changes to make once and have effect in all relevant places

What is implicit casting?

Implicit casting is the process of simply assigning one entity to another without any transformation guidance to the compiler. This type of casting is not permitted in all kinds of transformations and may not work for all scenarios.

Example

int i = 1000;

long j = i; //Implicit casting

Is sizeof a keyword in java?

The sizeof operator is not a keyword.

What is a native method?

A native method is a method that is implemented in a language other than Java.

In System.out.println(), what is System, out and println?

System is a predefined final class, out is a PrintStream object and println is a built-in overloaded method in the out object.

What are Encapsulation, Inheritance and Polymorphism

Or

Explain the Polymorphism principle. Explain the different forms of Polymorphism.

Polymorphism in simple terms means one name many forms. Polymorphism enables one entity to be used as a general category for different types of actions. The specific action is determined by the exact nature of the situation.

Polymorphism exists in three distinct forms in Java:
• Method overloading
• Method overriding through inheritance
• Method overriding through the Java interface

What is explicit casting?

Explicit casting in the process in which the complier are specifically informed to about transforming the object.

Example

long i = 700.20;

int j = (int) i; //Explicit casting

What is the Java Virtual Machine (JVM)?

The Java Virtual Machine is software that can be ported onto various hardware-based platforms

What do you understand by downcasting?

The process of Downcasting refers to the casting from a general to a more specific type, i.e. casting down the hierarchy

What are Java Access Specifiers?

Or

What is the difference between public, private, protected and default Access Specifiers?

Or

What are different types of access modifiers?

Access specifiers are keywords that determine the type of access to the member of a class. These keywords are for allowing
privileges to parts of a program such as functions and variables. These are:
• Public : accessible to all classes
• Protected : accessible to the classes within the same package and any subclasses.
• Private : accessible only to the class to which they belong
• Default : accessible to the class to which they belong and to subclasses within the same package

Which class is the superclass of every class?

Object.

Name primitive Java types.

The 8 primitive types are byte, char, short, int, long, float, double, and boolean.

What is the difference between static and non-static variables?

Or

What are class variables?

Or

What is static in java?

Or

What is a static method?

A static variable is associated with the class as a whole rather than with specific instances of a class. Each object will share a common copy of the static variables i.e. there is only one copy per class, no matter how many objects are created from it. Class variables or static variables are declared with the static keyword in a class. These are declared outside a class and stored in static memory. Class variables are mostly used for constants. Static variables are always called by the class name. This variable is created when the program starts and gets destroyed when the programs stops. The scope of the class variable is same an instance variable. Its initial value is same as instance variable and gets a default value when its not initialized corresponding to the data type. Similarly, a static method is a method that belongs to the class rather than any object of the class and doesn’t apply to an object or even require that any objects of the class have been instantiated.
Static methods are implicitly final, because overriding is done based on the type of the object, and static methods are attached to a class, not an object. A static method in a superclass can be shadowed by another static method in a subclass, as long as the original method was not declared final. However, you can’t override a static method with a non-static method. In other words, you can’t change a static method into an instance method in a subclass.

Non-static variables take on unique values with each object instance.

What is the difference between the boolean & operator and the && operator?

If an expression involving the boolean & operator is evaluated, both operands are evaluated, whereas the && operator is a short cut operator. When an expression involving the && operator is evaluated, the first operand is evaluated. If the first operand returns a value of true then the second operand is evaluated. If the first operand evaluates to false, the evaluation of the second operand is skipped.

How does Java handle integer overflows and underflows?

It uses those low order bytes of the result that can fit into the size of the type allowed by the operation.

What if I write static public void instead of public static void?

Program compiles and runs properly.

What is the difference between declaring a variable and defining a variable?

In declaration we only mention the type of the variable and its name without initializing it. Defining means declaration + initialization. E.g. String s; is just a declaration while String s = new String (”bob”); Or String s = “bob”; are both definitions.

What type of parameter passing does Java support?

In Java the arguments (primitives and objects) are always passed by value. With objects, the object reference itself is passed by value and so both the original reference and parameter copy both refer to the same object.

Explain the Encapsulation principle.

Encapsulation is a process of binding or wrapping the data and the codes that operates on the data into a single entity. This keeps the data safe from outside interface and misuse. Objects allow procedures to be encapsulated with their data to reduce potential interference. One way to think about encapsulation is as a protective wrapper that prevents code and data from being arbitrarily accessed by other code defined outside the wrapper.

What do you understand by a variable?

Variable is a named memory location that can be easily referred in the program. The variable is used to hold the data and it can be changed during the course of the execution of the program.

What do you understand by numeric promotion?

The Numeric promotion is the conversion of a smaller numeric type to a larger numeric type, so that integral and floating-point operations may take place. In the numerical promotion process the byte, char, and short values are converted to int values. The int values are also converted to long values, if necessary. The long and float values are converted to double values, as required.

What do you understand by casting in java language? What are the types of casting?

The process of converting one data type to another is called Casting. There are two types of casting in Java; these are implicit casting and explicit casting.

What is the first argument of the String array in main method?

The String array is empty. It does not have any element. This is unlike C/C++ where the first element by default is the program name. If we do not provide any arguments on the command line, then the String array of main method will be empty but not null.

How can one prove that the array is not null but empty?

Print array.length. It will print 0. That means it is empty. But if it would have been null then it would have thrown a NullPointerException on attempting to print array.length.

Can an application have multiple classes having main method?

Yes. While starting the application we mention the class name to be run. The JVM will look for the main method only in the class whose name you have mentioned. Hence there is not conflict amongst the multiple classes having main method.

When is static variable loaded? Is it at compile time or runtime? When exactly a static block is loaded in Java?

Static variable are loaded when classloader brings the class to the JVM. It is not necessary that an object has to be created. Static variables will be allocated memory space when they have been loaded. The code in a static block is loaded/executed only once i.e. when the class is first initialized. A class can have any number of static blocks. Static block is not member of a class, they do not have a return statement and they cannot be called directly. Cannot contain this or super. They are primarily used to initialize static fields.

Can I have multiple main methods in the same class?

We can have multiple overloaded main methods but there can be only one main method with the following signature :

public static void main(String[] args) {}

No the program fails to compile. The compiler says that the main method is already defined in the class.

Explain working of Java Virtual Machine (JVM)?

JVM is an abstract computing machine like any other real computing machine which first converts .java file into .class file by using Compiler (.class is nothing but byte code file.) and Interpreter reads byte codes.

How can I swap two variables without using a third variable?

Add two variables and assign the value into First variable. Subtract the Second value with the result Value. and assign to Second variable. Subtract the Result of First Variable With Result of Second Variable and Assign to First Variable. Example:

int a=5,b=10;a=a+b; b=a-b; a=a-b;

An other approach to the same question

You use an XOR swap.

for example:

int a = 5; int b = 10;
a = a ^ b;
b = a ^ b;
a = a ^ b;

What is data encapsulation?

Encapsulation may be used by creating ‘get’ and ’set’ methods in a class (JAVABEAN) which are used to access the fields of the object. Typically the fields are made private while the get and set methods are public. Encapsulation can be used to validate the data that is to be stored, to do calculations on data that is stored in a field or fields, or for use in introspection (often the case when using javabeans in Struts, for instance). Wrapping of data and function into a single unit is called as data encapsulation. Encapsulation is nothing but wrapping up the data and associated methods into a single unit in such a way that data can be accessed with the help of associated methods. Encapsulation provides data security. It is nothing but data hiding.

What is reflection API? How are they implemented?

Reflection is the process of introspecting the features and state of a class at runtime and dynamically manipulate at run time. This is supported using Reflection API with built-in classes like Class, Method, Fields, Constructors etc. Example: Using Java Reflection API we can get the class name, by using the getName method.

Does JVM maintain a cache by itself? Does the JVM allocate objects in heap? Is this the OS heap or the heap maintained by the JVM? Why

Yes, the JVM maintains a cache by itself. It creates the Objects on the HEAP, but references to those objects are on the STACK.

What is phantom memory?

Phantom memory is false memory. Memory that does not exist in reality.

Can a method be static and synchronized?

A static method can be synchronized. If you do so, the JVM will obtain a lock on the java.lang.
Class instance associated with the object. It is similar to saying:

synchronized(XYZ.class) {

}

What is difference between String and StringTokenizer?

A StringTokenizer is utility class used to break up string.

Example:

StringTokenizer st = new StringTokenizer(”Hello World”);

while (st.hasMoreTokens()) {

System.out.println(st.nextToken());

}

Output:

Hello

World
