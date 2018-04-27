import java.io.IOException;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class InsertTuplesClass {

	public static void main(String[] args) throws IOException {
		PrintWriter pw = new PrintWriter("C://디비작업/t1.sql");
		for(int i=1; i<=200; i++) {
			String data = "insert into table1 values("+i+");";
			pw.println(data);
		}
		pw.close();

	}
 
}
