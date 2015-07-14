import sys
import csv
import operator

#1. Which Region have the most State Universities?
def get_region_with_most_suc():
  f = open('suc_ph.csv', 'r')
  SUC = {}
  for index, line in enumerate(f):
    row = line.split(',')
    if row[0] in SUC:
      SUC[row[0]] += 1
    else:
      SUC[row[0]] = 1
  f.close()
  SUC_list = sorted(SUC.items(), key = operator.itemgetter(1), reverse = True)   
  print "1. The region with the most SUC is " + SUC_list[0][0]

#2. Which Region have the most enrollees?
def get_region_with_most_enrollees_by_school_year(school_year):
  f = open('suc_ph.csv', 'r')
  SUC = {}
  for index, line in enumerate(f):
    row = line.split(',')
    try:
      if (school_year == '2010-2011'):
        studs = int(row[2])
      elif (school_year == '2011-2012'):
        studs = int(row[3])
      elif(school_year == '2012-2013'):
        studs = int(row[4])
    except ValueError:
      studs = 0
    if row [0] in SUC:
       SUC[row[0]] += studs
    else:
       SUC[row[0]] = studs
  f.close()
  SUC_list = sorted(SUC.items(), key = operator.itemgetter(1), reverse = True)
  print "2. The region with the most SUC enrollees is " + SUC_list[0][0]

#3. Which Region have the most graduates?
def get_region_with_most_graduates_by_school_year(school_year):
  f = open('suc_ph.csv', 'r')
  SUC = {}
  for index, line in enumerate(f):
    row = line.split(',')
    try:
      if (school_year == '2009-2010'):
        studs = int(row[5])
      elif (school_year == '2010-2011'):
        studs = int(row[6])
      elif(school_year == '2011-2012'):
        studs = int(row[7])
    except ValueError:
      studs = 0 
    if row [0] in SUC:
       SUC[row[0]] += studs
    else:
       SUC[row[0]] = studs
  f.close()
  SUC_list = sorted(SUC.items(), key = operator.itemgetter(1), reverse = True)
  print "3. The region with the most SUC graduates is " + SUC_list[0][0]

#4 top 3 SUC who has the chepeast tuition fee by schoolyear
def get_top_3_cheapest_by_school_year(level, school_year):
  f = open('tuitionfeeperunitsucproglevel20102013.csv', 'r')
  SUC = {}
  for index, line in enumerate(f):
    row = line.split(',')
    if (level == 'BS'):
      try:
        if (school_year == '2010-2011'):
          studs = int(row[2])
        elif (school_year == '2011-2012'):
          studs = int(row[5])
        elif(school_year == '2012-2013'):
          studs = int(row[8])
      except ValueError:
        studs = 0
    if (level == 'MS'):
      try:
        if (school_year == '2010-2011'):
          studs = int(row[3])
        elif (school_year == '2011-2012'):
          studs = int(row[6])
        elif(school_year == '2012-2013'):
          studs = int(row[9])
      except ValueError:
        studs = 0
    if (level == 'PHD'):
      try:
        if (school_year == '2010-2011'):
          studs = int(row[4])
        elif (school_year == '2011-2012'):
          studs = int(row[7])
        elif(school_year == '2012-2013'):
          studs = int(row[10])
      except ValueError:
        studs = 0

    if row [1] in SUC:
       SUC[row[1]] += studs
    else:
       SUC[row[1]] = studs
  del_SUC = []
  for key in SUC:
    if(SUC[key] == 0):
      del_SUC.append(key)

  for val in del_SUC:
    del SUC[val]
  f.close()

  SUC_list = min(SUC, key = SUC.get)
  print "4. Top 3 cheapest SUC for BS level in school year 2010-2011"
  print "  1.", SUC_list, SUC[SUC_list]
  del SUC[SUC_list]
  SUC_list = min(SUC, key = SUC.get)
  print "  2.", SUC_list, SUC[SUC_list]
  del SUC[SUC_list]
  SUC_list = min(SUC, key = SUC.get) 
  print "  3.", SUC_list, SUC[SUC_list] 

#5 top 3 SUC who has the most expensive tuition fee by schoolyear
def get_top_3_most_expensive_by_school_year(level, school_year):
  f = open('tuitionfeeperunitsucproglevel20102013.csv', 'r')
  SUC = {}
  for index, line in enumerate(f):
    row = line.split(',')
    if (level == 'BS'):
      try:
        if (school_year == '2010-2011'):
          studs = int(row[2])
        elif (school_year == '2011-2012'):
          studs = int(row[5])
        elif(school_year == '2012-2013'):
          studs = int(row[8])
      except ValueError:
        studs = 0
    if (level == 'MS'):
      try:
        if (school_year == '2010-2011'):
          studs = int(row[3])
        elif (school_year == '2011-2012'):
          studs = int(row[6])
        elif(school_year == '2012-2013'):
          studs = int(row[9])
      except ValueError:
        studs = 0
    if (level == 'PHD'):
      try:
        if (school_year == '2010-2011'):
          studs = int(row[4])
        elif (school_year == '2011-2012'):
          studs = int(row[7])
        elif(school_year == '2012-2013'):
          studs = int(row[10])
      except ValueError:
        studs = 0

    if row [1] in SUC:
       SUC[row[1]] += studs
    else:
       SUC[row[1]] = studs
  del_SUC = []
  for key in SUC:
    if(SUC[key] == 0):
      del_SUC.append(key)

  for val in del_SUC:
    del SUC[val]
  f.close()

  SUC_list = max(SUC, key = SUC.get)
  print "5. Top 3 expensive SUC for BS level in school year 2010-2011"
  print "  1.", SUC_list, SUC[SUC_list], "per unit"
  del SUC[SUC_list]
  SUC_list = max(SUC, key = SUC.get)
  print "  2.", SUC_list, SUC[SUC_list]
  del SUC[SUC_list]
  SUC_list = max(SUC, key = SUC.get) 
  print "  3.", SUC_list, SUC[SUC_list] 

#6 list all SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013
def all_suc_who_have_increased_tuition_fee():
  f = open('tuitionfeeperunitsucproglevel20102013.csv', 'r')
  dic = []
  data = csv.reader(f)
  col = 2

  for row in data:
    try:
      if int(row[col+3]) > int(row[col]):
        dic.append(row[col-1])
      elif int(row[col+4]) > int(row[col+1]):
        dic.append(row[col-1])
      elif int(row[col+5]) > int(row[col+2]):
        dic.append(row[col-1])
      elif int(row[col+6]) > int(row[col]):
        dic.append(row[col-1])
      elif int(row[col+7]) > int(row[col+1]):
        dic.append(row[col-1])
      elif int(row[col+8]) > int(row[col+2]):
        dic.append(row[col-1])
      elif int(row[col+6]) > int(row[col]+3):
        dic.append(row[col-1])
      elif int(row[col+7]) > int(row[col+4]):
        dic.append(row[col-1])
      elif int(row[col+8]) > int(row[col+5]):
        dic.append(row[col-1])
    except Exception:
      pass
  print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013"
  ctr = 1
  for item in dic:
    print(" %d, %s") % (ctr, item)
    ctr += 1
  #print "   Technological University of the Philippines, Apayao State College, Marikina Polytechnic College, Surigao State College of Technolgoy"

#7 which discipline has the highest passing rate?
def get_discipline_with_highest_passing_rate_by_shool_year(school_year):
  f = open('performancesucprclicensureexam20102012.csv','r')
  data = csv.reader(f)
  passers = {}
  takers = {}
  rate  = {}
  if school_year == "2010":
    col = 3
  elif school_year == "2011":
    col = 4
  elif school_year == "2012":
    col = 5
  else:
    print "7. ERROR! Not included in tha database"
    return 0

  for row in data:
    try:
      if passers.has_key(row[2]) and row[2] != "Total" and row[2] != "-":
        passers[row[2]] += int(row[col])
        takers[row[2]] += int(row[col+4])
      else:
        passers[row[2]] = int(row[col])
        takers[row[2]] = int(row[col+4])
    except Exception:
      pass
  for d in passers:
    try:
      if d != "-":
        rate[d] = (float(takers[d] -  float(passers[d]))/float(takers[d]))
    except Exception:
      pass
  print("7. The discipline which has the highest passing rate is %s") % ((sorted(rate.items(), key=lambda (n,m): (-m,n)))[0][0])
  

#8 list top 3 SUC with the most passing rate by discipline by school year
def get_top_3_suc_performer_by_discipline_by_year(discipline, school_year):
  f = open('performancesucprclicensureexam20102012.csv','r')
  data = csv.reader(f)
  passers = {}
  takers = {}
  rate  = {}
  if school_year == "2010":
    col = 3
  elif school_year == "2011":
    col = 4
  elif school_year == "2012":
    col = 5
  else:
    print "8. ERROR! Not included in tha database"
    return 0

  for row in data:
    try:
      if row[2] == discipline:
        if passers.has_key(row[1]):
          passers[row[1]] += int(row[col])
          takers[row[1]] += int(row[col+4])
        else:
          passers[row[1]] = int(row[col])
          takers[row[1]] = int(row[col+4])
    except Exception:
      pass
  for d in passers:
    try:
      if d != "-" and (passers[d]) != 0:
        rate[d] = (float(takers[d] -  float(passers[d]))/float(takers[d]))
    except Exception:
      pass
  print("8. list top 3 SUC with the most passing rate by discipline by school year")
  print(" 1. %s") % ((sorted(rate.items(), key=lambda (n,m): (-m,n)))[0][0])
  print(" 2. %s") % ((sorted(rate.items(), key=lambda (n,m): (-m,n)))[1][0])
  print(" 3. %s") % ((sorted(rate.items(), key=lambda (n,m): (-m,n)))[2][0])  


def main():
  get_region_with_most_suc()
  get_region_with_most_enrollees_by_school_year('2010-2011')
  get_region_with_most_graduates_by_school_year('2010-2011')
  get_top_3_cheapest_by_school_year('BS', '2010-2011')
  get_top_3_most_expensive_by_school_year('BS', '2010-2011')
  all_suc_who_have_increased_tuition_fee()
  get_discipline_with_highest_passing_rate_by_shool_year('2010')
  get_top_3_suc_performer_by_discipline_by_year('Accountancy', '2011')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
