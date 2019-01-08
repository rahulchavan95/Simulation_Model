import random
import matplotlib.pyplot as plt


#Arrival Distribution

min_time=[]
max_time=[]
min_time_limit=6
max_time_limit=24
no_of_patients=[]
prob=[0.008,0.076,0.157,0.188,0.099,0.130,0.221,0.111,0.010]
time_int_for_arr=min_time_limit
cumulative_prob=[]
tag_num_min=[]
tag_num_max=[]
cnt=0
cnt1=0
no_of_events=30
sim_calculation=[]
analytical_cal=[]



no_of_patients=[4,37,76,91,48,63,107,54,5] 
sum_of_patient=sum(map(int,no_of_patients))

i=0

##################################################Calculating cumulative probability for Arrival##################################################
while(time_int_for_arr>=min_time_limit and time_int_for_arr<max_time_limit):
  min_time.append(time_int_for_arr)
  max_time.append(int(min_time[len(min_time)-1])+2)
  
  if i==0:
	cumulative_prob.append(round(float(prob[i]),3))
	tag_num_min.append(i)
  else:
        cumulative_prob.append(round(float(cumulative_prob[i-1]+prob[i]),3))
	tag_num_min.append(int(cumulative_prob[i-1]*1000))
  tag_num_max .append(int(round(cumulative_prob[i]*1000-1,4)))
  i+=1
  time_int_for_arr+=2
prob=[float(i) for i in prob]
sum_of_prob=sum(prob)

    

print "\n\t\t\tTag number table for Arrival distribution\n"


print("Sr.No"+"\t"+"Time"+"\t\tNo_of_Patients"+"\t\tProbability"+"\tCumulative_Probabilty"+"\tTag_Numbers")


for i in range(len(prob)):                              #Arrival Distribution
 cnt+=1
 print(str(cnt)+"\t"+str(min_time[i])+"-"+str(max_time[i])+"\t\t\t"+str(no_of_patients[i])+"\t\t"+str(prob[i])+"\t\t\t"+str(cumulative_prob[i])+"\t\t   "+str(tag_num_min[i])+"-"+str(tag_num_max[i]))




# Service distribution

min_ser_time=[]
max_ser_time=[]
min_ser_time_limit=4
max_ser_time_limit=32
no_of_patients_for_ser=[]
prob_ser=[0.077,0.108,0.231,0.202,0.185,0.117,0.050,0.030]
time_int_for_ser=0
cumulative_prob_ser=[]
tag_num_min_ser=[]
tag_num_max_ser=[]
time_diff=4



#for i in range(1,9):
 #no_of_patients_for_ser.append(random.randint(1,110))
no_of_patients_for_ser=[5,7,15,13,12,7,3,2] 
sum_of_patient_for_ser=sum(map(int,no_of_patients_for_ser))



##################################################Calculating cumulative probability for SERVICE##################################################
i=0
while(time_int_for_ser>=0 and time_int_for_ser<max_ser_time_limit):
  
  min_ser_time.append(time_int_for_ser)
  
  max_ser_time.append(int(min_ser_time[len(min_ser_time)-1])+4)
 
  #i+=1
  #k+=2

  if i==0:
	cumulative_prob_ser.append(round(float(prob_ser[i]),3))
	tag_num_min_ser.append(i)
  else:
        cumulative_prob_ser.append(round(float(cumulative_prob_ser[i-1]+prob_ser[i]),3))
	tag_num_min_ser.append(int(cumulative_prob_ser[i-1]*1000))
  tag_num_max_ser.append(int(round(cumulative_prob_ser[i]*1000-1,4)))
  i+=1
  time_int_for_ser+=time_diff

prob_ser=[float(i) for i in prob_ser]
sum_of_prob_ser=sum(prob_ser)
  




print "\n\n\t\t\tTag number table for Service distribution\n\n"


print("Sr.No"+"\t"+"Time"+"\t\tNo_of_Patients"+"\t\tProbability"+"\tCumulative_Probabilty"+"\tTag_Numbers")


for i in range(len(prob_ser)):                                    #Service Distribution
 cnt1+=1
 print(str(cnt1)+"\t"+str(min_ser_time[i])+"-"+str(max_ser_time[i])+"\t\t\t"+str(no_of_patients_for_ser[i])+"\t\t"+str(prob_ser[i])+"\t\t\t"+str(cumulative_prob_ser[i])+"\t\t   "+str(tag_num_min_ser[i])+"-"+str(tag_num_max_ser[i]))



#Simulation Table"

random_no_of_arrival=[]	
inter_Arrival_Time=[]
arrival_time=[]
random_no_of_service=[]
service_begins=[]
service_time=[]
service_ends=[]
waiting_time_in_queue=[]
waiting_time_in_medical_centre=[]
idle_time_of_doctor=[]
queue_length=[]




index=0
for i in range(1,no_of_events+1):                     #generate random numbers           
  random_no_of_arrival.append(random.randint(1,1000))
  random_no_of_service.append(random.randint(1,1000))
  #random_no_of_arrival.append(lcg())
  #random_no_of_service.append(lcg())




def check_Arrival_range(n):                  #function to check arrival range 
 for i in range(0,len(tag_num_min)):
  #print min_ser_time[i],max_ser_time[i]
  if tag_num_min[i]<=n and n<=tag_num_max[i]:
   return i+1


def check_Service_range(n):                  #function to check service range
 for i in range(0,len(tag_num_min_ser)):
  #print min_ser_time[i],max_ser_time[i]
  if tag_num_min_ser[i]<=n and n<=tag_num_max_ser[i]:
   return i+1

def check_no(n):	                      #function to check digit
 if n=='-':
  return 0
 else:
  return n
 

def calculate_Average(list1):                 #function to calculate average

 list2=filter(lambda x: x!= '-',list1)
 list2=[float(i) for i in list2]
 #print str(sum(list2)),str(len(list1))
 return sum(list2)/len(list1)


def calculate_rate(list1):                   #function to calculate rate of arrival and service
 list2=filter(lambda x: x!= '-',list1)
 list2=[float(i) for i in list2]
 #print str(sum(list2)),str(len(list1))
 return len(list1)/sum(list2)



def calculate_sum(list1):                    #calculates sum 
 list2=filter(lambda x: x!= '-',list1)
 list2=[float(i) for i in list2]
 #print str(sum(list2)),str(len(list1))
 return sum(list2)




def chi_square_test(list1):                                              #chi square function for random no.
	check=100
	n=len(list1)
	N=sum(list1)
	sum1=0
	E=N//n
	for i in range(len(list1)):
		k=(list1[i]*E)*(list1[i]*E)
		p=k/E
		sum1+=p
	#print(check,sum1)
	if(check<sum1):
		return 1
	else:
		return 0



rand=1

def lcg():                                                             #function for random number generation
    a = 2
    c = 1
    m = 999
    global rand
    rand = (a*rand + c) % m
    return rand



m=0
while(m!=1):
	m=chi_square_test(random_no_of_arrival)

m=0
while(m!=1):
	m=chi_square_test(random_no_of_service)




##################################################Calculation of Simulation Table#########################################################

print "\n\n\t\t\t\tSimulation Table\n"


print "sr.no   r_nos_arr   inter_AT Arrival_time   r_nos_ser ser_begins service_time ser_ends wt_in_queue idle_time_of_doctor wtin_medical_centre Q_len"

for i in range(0,len(random_no_of_arrival)):
 if i==0:
  inter_Arrival_Time.append('-')
  arrival_time.append(float(min_time_limit))
  service_begins.append(float(min_time_limit))
  if float(service_begins[i])==float(min_time_limit):
   idle_time_of_doctor.append(0)
  else:
   idle_time_of_doctor.append(str(float(service_begins[i])-float(min_time_limit)))
 else:
  inter_Arrival_Time.append(check_Arrival_range(random_no_of_arrival[i])) 
  arrival_time.append(str(float(arrival_time[i-1])+float(float(inter_Arrival_Time[i])*0.01)))
  if float(arrival_time[i])>=float(service_ends[i-1]):
   #print "do",arrival_time[i]
   service_begins.append(arrival_time[i])
  else:
   service_begins.append(float(service_begins[i-1])+float(service_time[i-1])*0.01)
  '''
  if float(service_begins[i])==float(service_ends[i-1]):
   idle=0
   #print "idle=",idle,service_begins[i],service_ends[i-1]
  else:
   idle=(float(service_begins[i])-float(service_ends[i-1]))*100
   print "idle=",idle,service_begins[i],service_ends[i-1]
 # if idle<=0:
  # idle=0
  '''
  idle=(float(service_begins[i])-float(service_ends[i-1]))*100
  if(idle<=0):
   idle=0
  idle_time_of_doctor.append(str(idle))
   
 
 service_time.append(check_Service_range(random_no_of_service[i]))
 waiting_time_in_queue.append(str(float((float(service_begins[i])-float(arrival_time[i]))*100)))
 service_ends.append(str(float(service_begins[i])+float(service_time[i])*0.01))
 waiting_time_in_medical_centre.append((float(service_ends[i])-float(arrival_time[i]))*100)
 if float(waiting_time_in_queue[i])==0:
   queue_length.append('-')
 else:
   queue_length.append(1)


cnt2=0



for i in range(0,len(random_no_of_arrival)):                              #Prints Simulation Table
  cnt2+=1
  print  str(cnt2)+"\t"+str(random_no_of_arrival[i])+"\t\t"+str(inter_Arrival_Time[i])+"\t"+ str(arrival_time[i])+"\t\t"+str(random_no_of_service[i])+"\t"+str(service_begins[i])+"\t\t"+str(service_time[i])+"\t"+service_ends[i]+"\t"+waiting_time_in_queue[i]+"\t\t"+str(idle_time_of_doctor[i])+"\t\t"+str(waiting_time_in_medical_centre[i])+"\t\t    "+str(queue_length[i])



#############################################################ASimulation Calculation##############################################################

#Simulation Calculation


avg_wt_in_q=calculate_Average(waiting_time_in_queue)                       #Average time of patient in queue
avg_Q_len=calculate_Average(queue_length)                                  #Average queue length 
avg_wt_t_mcentre=calculate_Average(waiting_time_in_medical_centre)         #Average time of patient in medical centre
avg_of_idle_t_doctor=calculate_Average( idle_time_of_doctor)               #Idle time of doctor
arrival_rate=calculate_rate(inter_Arrival_Time)                            #Arrival Rate
service_rate=calculate_rate(service_time)                                  #Service Rate


print "\n\n\tSimulation Calculation\n"

print "Average Queue Length = ",avg_Q_len                                            
print "Average Waiting Time of a Patient in Queue = ",avg_wt_in_q
print "Average Waiting Time of a Patient in a Medical Centre = ",avg_wt_t_mcentre
print "Arrival rate = ",arrival_rate
print "Service rate = ",service_rate
print "Idle Time of a Doctor = ",avg_of_idle_t_doctor
print "\n"




#############################################################Analytical Calculation##############################################################





lambdaa=1/(float(no_of_events-1))                   #Arrival rate of Math Calc.
mu=1/float(time_diff)                               #Service rate of Math Calc.
avg_wt_in_q1=lambdaa/(mu*(mu-lambdaa))              #Avg wt time of patient in queue
avg_wt_t_mcentre1=1/(mu-lambdaa)                    #Avg wt time of patient in system
avg_Q_len1=(round(lambdaa*avg_wt_in_q1,3))          #Queue length of Math Calc.
# arrival rate * waiting time in the queue




print "\n\n\tAnalytical Calculation\n"
print "Arrival rate = ",lambdaa
print "Service rate = ",mu
print "Average Waiting Time of a patient in Queue = ",avg_wt_in_q1
print "Average Waiting Time of a Patient in a Medical Centre = ",avg_wt_t_mcentre1
print "Queue Length = ",avg_Q_len1
print "\n"




######################################################Plotting Graph using matplotlib##############################################################


fig=plt.figure()


value1=[arrival_rate,avg_Q_len]                                             #Comparison of Arrival Rate and Queue length
values2=[lambdaa,avg_Q_len1]
names=["Arrival Rate","Queue Length"]
ax1 = fig.add_subplot(321)
ax1.set_title("Comparison of Arrival rate with Queue Length")
ax1.plot(names,value1, label='Simulation',marker='o')
ax1.plot(names, values2, label='Analytical',marker='o')
leg = plt.legend( loc = 'upper left')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)



Service_value1=[service_rate,avg_Q_len]                                    #Comparison of Service rate with Queue Length
Queue_value2=[mu,avg_Q_len1]
Service_Queue=["Service Rate","Queue Length"]
ax2 = fig.add_subplot(322) 
ax2.set_title("Comparison of Service rate with Queue Length")
ax2.plot(Service_Queue,Service_value1, label="Simulation",marker='o')
ax2.plot(Service_Queue, Queue_value2, label="Analytical",marker='o')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)




arrival_rate_value1=[arrival_rate,service_rate]                           #Comparison of Arrival rate with Service Rate                        
ser_rate_values2=[lambdaa,mu]
plot_names=["Arrival Rate","Service Rate"]
ax3 = fig.add_subplot(323)
ax3.set_title("Comparison of Arrival rate with Service Rate")
ax3.bar(plot_names,arrival_rate_value1, label="Simulation")
ax3.bar(plot_names, ser_rate_values2, label="Analytical")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)




avg_wt_que=[avg_wt_in_q,avg_wt_t_mcentre]                                #Comparison of waiting time of patient in queue and medical 
avg_wt_medical=[avg_wt_in_q1,avg_wt_t_mcentre1]
avg_plot_names=["AvgWT_Q","AvgWT_Sys"]
ax4=fig.add_subplot(324)
ax4.set_title("Comparison of Avg WT in Q And Avg WT in System");
ax4.bar(avg_plot_names,avg_wt_que, label="Simulation")
ax4.bar(avg_plot_names, avg_wt_medical, label="Analytical")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)




sim_value=[service_rate,avg_wt_in_q,avg_wt_t_mcentre]                    #Comparison of Simlation Calculation And Analytical Calculation
an_value=[mu,avg_wt_in_q1,avg_wt_t_mcentre1]
sim_ant=["S_Rt","A_WT_Q","A_WT_M"]
ax5=fig.add_subplot(325)
ax5.set_title("Comparison of Simlation Calculation And Analytical Calculation");
ax5.bar(sim_ant,sim_value, label="Simulation")
ax5.bar(sim_ant,an_value, label="Analytical")



plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout(pad=1.0, w_pad=1.0, h_pad=2.5)
plt.show()

