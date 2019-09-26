import sys
import re

class Line:
      def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.x = "NA"
        if p2[0]- p1[0] == 0:
          self.m = 'v'
          self.b = 'v'
          self.x = p1[0]
        else:
          # Cast one of the integer to float to convert 
          self.m = (float(p2[1]) - p1[1]) / (p2[0]- p1[0])
          self.b = float(p1[1]) - self.m * p1[0]

def euclidean_distance(p1, p2):
  return ((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2) ** (0.5)

def check_intersection(p1, p2, p3, p4):
  # check to make sure line 1 != line 2! can check this in input 
  line1 = Line(p1,p2)
  line2 = Line(p3,p4)
  #maybe check if input is of type line?
  if line2.m - line1.m == 0 and line1.b != line2.b:
    return False
  # elif line2.m - line1.m == 0 and line1.b == line2.b:
  #   if max(line1.p1[0],line1.p2[0]) < 
  elif line1.m == 'v':
    x = line1.x
    y = line2.m * x + line2.b
  elif line2.m == 'v':
    x = line2.x
    y = line1.m * x + line1.b
  else:
    x = (float(line2.b)-line1.b) / (line1.m - line2.m)
    y = line1.m * x + line1.b
  
  # print("Print x: " + str(x))
  # print("Print y: " + str(y))

  if y > max(line1.p1[1], line1.p2[1]) or y < min(line1.p1[1], line1.p2[1]):
    return False
  elif y > max(line2.p1[1], line2.p2[1]) or y < min(line2.p1[1], line2.p2[1]):
    return False
  return (x, y)

def build_graph(streets):
  #check that streets is a dic
  street_list = streets.values()
  print(street_list)
  V = {}
  E = []
  # A list that stores how many intersections occurred between each node p1 and p2, and p3 and p4.
  I = {} 
  vertex_id = 1
  # Iterate through the first n-1 streets
  for i in range(len(street_list)-1):
    street1 = street_list[i]
    # From street i, iterate through connected nodes on that street. These are the jth node and j+1th node.
    for j in range(len(street1) - 1):
      p1 = street1[j]
      p2 = street1[j+1]
      # A counter that first selects the i+1th street and 
      # then iterates until the nth street.
      street_count = i + 1
      # While we haven't finished comparing p1 and p2 with
      # every valid pair of nodes from the i+1 street to  
      # the nth street.
      while street_count <= len(street_list) - 1:
        street2 = street_list[street_count]
        # Iterate through all valid node pairs in street2 
        # and compare with p1 and p2.
        for k in range(len(street2) - 1):
          p3 = street2[k]
          p4 = street2[k+1]
          print("")
          print(p1)
          print(p2)
          print(p3)
          print(p4)
          print("")
          intersection = check_intersection(p1, p2, p3, p4)
          # If there is an intersection, add the 
          # nodes that have not already been added to the
          # vertices dictionary to the dictionary,
          # including the intersection node.
          print("V_values: ")
          print(V)
          if intersection:
            V_values = V.values()
            if intersection in V_values:
              for key, value in V.items():
                if value == intersection:
                  intersection_id = key
                  break
            print("V_values: ")
            print(V)
            V_values = V.values()
            if not intersection in V_values:
              V[vertex_id] = intersection
              intersection_id = vertex_id
              vertex_id = vertex_id + 1
            print("V_values: ")
            print(V)
            V_values = V.values()
            if p1 in V_values:
              for key, value in V.items():
                if value == p1:
                  p1_id = key
                  break
            if not p1 in V_values:
              V[vertex_id] = p1
              p1_id = vertex_id
              vertex_id = vertex_id + 1
            print("V_values: ")
            print(V)
            V_values = V.values()
            if p2 in V_values:
              for key, value in V.items():
                if value == p2:
                  p2_id = key
                  break
            if not p2 in V_values:
              V[vertex_id] = p2
              p2_id = vertex_id
              vertex_id = vertex_id + 1
            print("V_values: ")
            print(V)
            # Make sure that the edge is unique and that the point is not equal to the intersection!
            if not (p1_id, intersection_id) in E and p1 != intersection:
              E.append((p1_id, intersection_id))
            if not (p2_id, intersection_id) in E and p2 != intersection:
              E.append((p2_id, intersection_id))

            if (p1_id,p2_id) in I.keys():
              d = euclidean_distance(p1, intersection)
              I[(p1_id,p2_id)][intersection_id] = d
            if not (p1_id,p2_id) in I.keys():
              d = euclidean_distance(p1, intersection)
              I[(p1_id,p2_id)] = {intersection_id: d}
            V_values = V.values()
            if p3 in V_values:
              for key, value in V.items():
                if value == p3:
                  p3_id = key
                  break
            if not p3 in V_values:
              V[vertex_id] = p3
              p3_id = vertex_id
              vertex_id = vertex_id + 1
            V_values = V.values()
            if p4 in V_values:
              for key, value in V.items():
                if value == p4:
                  p4_id = key
                  break
            if not p4 in V_values:
              V[vertex_id] = p4
              p4_id = vertex_id
              vertex_id = vertex_id + 1

            if not (p3_id, intersection_id) in E and p3 != intersection:
              E.append((p3_id, intersection_id))
            if not (p4_id, intersection_id) in E and p4 != intersection:
              E.append((p4_id, intersection_id))

       
            if (p3_id,p4_id) in I.keys():
              d = euclidean_distance(p3, intersection)
              I[(p3_id,p4_id)][intersection_id] = d
            if not (p3_id,p4_id) in I.keys():
                d = euclidean_distance(p3, intersection)
                I[(p3_id,p4_id)] = {intersection_id: d}
            
        # Iterate the street counter by 1 so we are comparing p1 and p2
        # to the nodes in the next street in street_list.
       
        street_count = street_count + 1
  # Each key is the tuple (p1,p2) and each value is
  # a dictionary of intersection id and distance to p1
  # key-value pairs.
  # E.g. key ((1,3),(2,4)), and value {1: 3, 2: 1}

  for key, value in I.items():
    if len(value.values()) >= 2:
      p1 = key[0]
      p2 = key[1]

      # If euclidean distance is equal to 0
      # then p1 is an intersection
      # if euclidean distance is equal to max 
      # distance . then p2 is an intersection
        
      # key2 is the vertex id of each intersection
      # value2 is the euclidean distance from the 
      # intersection to p1
  
      # returns a sorted array of tuples, sorted 
      # by the second value in the array 
      sorted_value = sorted(value.items(), key=lambda x: x[1])
              
      for i in range(len(sorted_value)):
        if (p1, sorted_value[i][0]) in E:
          E.remove((p1, sorted_value[i][0]))
        if (p2, sorted_value[i][0]) in E:
          E.remove((p2, sorted_value[i][0]))
            
      for i in range(len(sorted_value)):
        if (sorted_value[0][1]) == 0:
          intersection1 = (p1, sorted_value[1][0])
          E.append(intersection1)
          for i in range(len(sorted_value)):
            if i + 2 > len(sorted_value):
              E.append((sorted_value[i+1][0],sorted_value[i+2][0]))
            else:
              E.append((sorted_value[i+1][0],p2))
        else: 
          intersection1 = (p1, sorted_value[0][0])
          E.append(intersection1)
          for i in range(len(sorted_value)):
            if i == len(sorted_value) - 1:
              E.append((sorted_value[i][0],p2))
              break
      
            E.append((sorted_value[i][0],sorted_value[i+1][0]))
     
  E_clean = list(dict.fromkeys(E))  

  return (V,E_clean)

def main():
    # streets = {"Street 1": [(2,-1),(2,2),(5,5),(5,6),(3,8)], "Street 2": [(4,2),(4,8)], "Street3": [(1,4),(5,8)]}
    # g = check_intersection((3, 4), (5, 4), (2, 1), (3, 4))
    # print(g)

    # p = Line((2,1),(3,4))
    # h = Line((2,4),(5,4))
    # print("p.m = " + str(p.m) + " p.b = " + str(p.b))
    # print("h.m = " + str(h.m) + " h.b = " + str(h.b))
    #A dictionary containing all the streets
    streets = {}
    while True:
      line = sys.stdin.readline()

      user_input = re.compile("([acrg])\s(\".+\")\s").split(line)

      print(user_input)
      
      # street_name = user_input[2]
      street_name_test = re.findall("\"[^\s].+[^\s]\"", line)
      if street_name_test[0] != user_input[2]:
        sys.stderr.write("Error: Invalid street name.\n")
        continue
      
      # Test if street name has special characters in it
      street_name_test2 = re.findall("[^a-zA-Z\s\"]", user_input[2])
      print(street_name_test2)
      street_name_test2.append(0)
      print(street_name_test2)
      print(len(street_name_test2))
      if len(street_name_test2) > 1:
        sys.stderr.write("Error: Only alphabetical characters are allowed for street names.\n")
        continue


      # Street names are case-insensitive
      # for key in streets.keys():
      #   if lower(street_name) == lower(key):
      #     street_name = key

      

      # Make sure the input coordinates for the nodes in the street were input properly.
      coordinates = user_input[3]
       
      coordinates_test = re.findall("^((\(-?\d*\,-?\d*\))*)$", coordinates)
      format_coordinates = re.sub("\s","", user_input[3])
      print(coordinates)
      print(coordinates_test)
      print(format_coordinates)
      if coordinates_test[0][0] != format_coordinates:
        sys.stderr.write("Error: Invalid input.\n")
        continue
      # except:
      #   sys.stderr.write("Error: Invalid input.\n")
      #   continue
      
     
      if len(user_input) == 1:
        command = re.sub('[^g]*',"",user_input[0]) 
        if command != 'g':
          sys.stderr.write("Error: Invalid input.\n")
          continue

      else:
        command = re.sub('[^acr]',"", user_input[1])
        if len(command) == 0 or len(command) > 1:
          sys.stderr.write("Error: Invalid input.\n")
          continue
  
      
      if command == 'a':
      
        if user_input[2][0] == " " or user_input[2][len(user_input[2])-1] == " ":
          sys.stderr.write("Error: Spaces are not allowed at the beginning or end of the street name.\n")
          continue
        
        street_name = re.sub('\"', "", user_input[2])
        t = re.sub('\D', "", user_input[3])
        vertices = []
        counter = 0
        for i in range(len(t)/2):
          vertices.append((int(t[i + counter]),int(t[i + counter + 1])))
          streets[street_name] = vertices
          counter = counter + 1

      elif command == 'c':
        street_name = re.sub('\"', "", user_input[2])

        try:
          del streets[street_name]
        except:
          sys.stderr.write("Error: " + street_name + " does not exist.\n")
          continue

        # if not street_name in streets.keys():
        #   sys.stderr.write("Error: " + street_name + " does not exist.")
        #   break
        t = re.sub('\D', "", user_input[3])
        vertices = []
        counter = 0
        for i in range(len(t)/2):
          vertices.append((int(t[i + counter]),int(t[i + counter + 1])))
          counter = counter + 1
        streets[street_name] = vertices
       
      elif command == 'r':
        street_name = re.sub('\"', "", user_input[2])
        try:
          del streets[street_name]
        except:
          sys.stderr.write("Error: " + street_name + " does not exist.\n")
          continue
        
      elif command == 'g':
        if len(streets.values()) == 0:
          sys.stderr.write("Error: No streets have been specified.\n")
          continue
        else:
          t = build_graph(streets)
          print("V = {\n")
          for key, value in t[0].items():
            print(str(key) + ": " + "(" + "{0:.2f}".format(value[0]) + "," + "{0:.2f}".format(value[1]) + ")\n")
          print("}\n")
          print("E = {\n")
          for i in range(len(t[1])):
            if i < len(t[1]) - 1:
              print("<" + str(t[1][i][0]) + "," + str(t[1][i][1])+ ">,\n")
            elif i == len(t[1]) - 1:
              print("<" + str(t[1][i][0]) + "," + str(t[1][i][1])+ ">\n")
          print("}\n")  
  
        # if line == '':
        #     break
        # print 'read a line:', line

    print 'Finished reading input'
    # return exit code 0 on successful termination
    sys.exit(0)

if __name__ == '__main__':
    main()


# try:
# except AssertionError as error:
#     print(error)
#     print('The linux_interaction() function was not executed')
