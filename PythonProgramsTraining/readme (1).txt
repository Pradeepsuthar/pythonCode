Doc link : https://drive.google.com/drive/folders/1DT1SCgb3Yv7mRro5OyDskOdlajpm2ToQ

Regular Expression

1. It is a suqunece of special characters hat is used in pattern maching agianst a text Set of special characters is known as Regular Expression

2. Python provieds RE module to used functions and methods in perform in Regular Expression.

Meta characters: 

1. They are special characters with special meaning to used create a pattern known as Regular Expression.

.
^
$
*
+
?
\
-
[
]
{
}
(
)

Quantifiers

Greedy *
Reluctant ?
Possessive +
0 or more occurences
Exactly 0 or 1
1 or more occurences

Boundry Matchers
Beginnig ^
Ending $

methods
search(pattern,string,[flag=0])
match(pattern,string,[flag=0])
findall(pattern,string,[flag=0])
sub(pattern,replace,string,count=0,[flag=0])
compile(pattern,[flag=0])

Match versus Search
1. match checks for a match only at the Beginnig of the string, while search checks.

Regular Expression Flags
re.l
re.L
re.M
re.S
re.U
re.X

Special Characters Class
.   Match any characters except newline
\d  Match a digit:[0-9]
\d  Match a non-digit:[^0-9]
\s  Match a whitespace character:[\t\r\n\f]
\S  Match non-whitespace:[^\t\r\n\f]
\w  Match a single word character:[A-Za-z0-9...]
\W  Match a non-word character:[^A-Za-z0-9...]


[]  character Class
[^] substraction
-   range
()  group
{}  occurences
|   or



