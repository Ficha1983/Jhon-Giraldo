import java.io.*;
import java.net.*;

public class Main {
    public static void main(String[] args) throws Exception {
        URL url = new URL("http://localhost:8000/api/productos/");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");

        BufferedReader in = new BufferedReader(
            new InputStreamReader(conn.getInputStream()));
        String inputLine;
        StringBuilder content = new StringBuilder();

        while ((inputLine = in.readLine()) != null)
            content.append(inputLine);

        in.close();
        conn.disconnect();

        System.out.println(content.toString());
    }
}
