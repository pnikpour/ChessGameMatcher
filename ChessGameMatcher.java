
import java.util.regex.*;
import java.io.*;
import java.util.ArrayList;

public class ChessGameMatcher
{
   public static String PGN_FILE = "data/lichess_pgn.pgn";
   
   public static void main(String[] args) throws IOException
   {
      
      String regex = "^1.*\\.\\s\\w?\\w?\\w\\d(=\\w)?(\\s\\w?\\w?\\w\\d(=\\w)?)?#?";
      Pattern pattern = Pattern.compile(regex);
      BufferedReader r = new BufferedReader(new FileReader(PGN_FILE));
      ArrayList<String> games = new ArrayList<String>();
       
      // For each line of input, try matching in it.
      String line;
      int count = 0;
      while ((line = r.readLine()) != null)
      {
         // For each match in the line, extract and print it.
         Matcher m = pattern.matcher(line);
         while (m.find())
         {
            count++;
            // Get the starting position of the text
            int start = m.start(0);
            // Get ending position
            int end = m.end(0);
           
            String game = line.substring(start,end);
            games.add(game);
         }
      }
      
      System.out.println(games.size() + " games");
      boolean dupes = areThereDuplicates(games);
      System.out.println(dupes);
   }
   
   public static boolean areThereDuplicates(ArrayList<String> games)
   {
      boolean dupes = false;
      for (int i = 0; i < games.size(); i++)
      {
         for (int k = i+1; k < games.size(); k++)
         {
            if (games.get(i).equalsIgnoreCase(games.get(k)))
            {
               System.out.println(i + "\t" + games.get(i));
               System.out.println(k + "\t" + games.get(k));
               dupes = true;
            }
         }
      }
      return dupes;
   }
}