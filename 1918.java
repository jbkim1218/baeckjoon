import java.util.*;
 
public class Main {    
 
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
 
        char[] calculation = scan.nextLine().toCharArray();
        
        Stack<Character> op = new Stack<>(); // 연산자를 담을 스택
        StringBuilder sb = new StringBuilder();//정답을 담을 문자열
        for(int i = 0; i < calculation.length; i++) {
            // 연산식이 숫자라면 그대로 문자열에 담아준다.
            if(calculation[i] >= 'A' && calculation[i] <= 'Z') sb.append(calculation[i] + "");
            else { //연산식이 숫자가 아니라면
                if(calculation[i] == '(') op.push(calculation[i]);
                else if(calculation[i] == ')') { //'('이 나올때까지 문자열에 담아준다.
                    while(!op.isEmpty() && op.peek() != '(') {
                        sb.append(op.pop()); //괄호가 아니면 연산자를 꺼내어 문자열에 담는다.
                    }
                    if(!op.isEmpty()) op.pop(); //'('연산자를 꺼내준다.
                }
                else { // + - / * 연산자 일경우
                    while(!op.isEmpty() && precedence(op.peek()) >= precedence(calculation[i])) {
                        sb.append(op.pop());
                    }
                    op.push(calculation[i]);
                }
            }
        }
        //스택에 있는 남은 연산자를 모두 꺼낸다.
        while(!op.isEmpty()) {
            sb.append(op.pop());
        }
        System.out.println(sb);
    }
   
    public static int precedence(char op) {
        if(op == '*' || op == '/') return 2;
        else if(op == '+' || op == '-') return 1;
        else return 0;
    }
}
