from datetime import datetime
import asyncio
import mysql.connector as con

is_server_up = False
a = ''

def decode(message):

    msg = ''.join(map(str, message))

    data = []
    
    print(msg)
  
    type_of_message = msg.split('#')[1]
    msg = msg.split('#')[2]
        
    print (msg)
    
    calls = msg.split(';')
    
    
   
    print (len(calls))
    
    if (len(calls) == 16): #full message
    
        data.append(type_of_message)
        data.append(calls[0]) #date
        data.append(calls[1]) #time
        data.append(calls[2] + calls[3]) #lat
        data.append(calls[4] + calls[5]) #lot
        #if (calls[6] != ''):
        data.append(calls[6])   #speed
        data.append(calls[7])   #course
        data.append(calls[8])   #height 
        data.append(calls[9])   #sats
        data.append(calls[10])  #hdops
        data.append(calls[11])  #inputs
        data.append(calls[12])  #outputs
        data.append(calls[13])  #adc
        data.append(calls[14])  #ibutton
        data.append(calls[15])  #params
    
        
        try:
            cursor.execute('INSERT into rango_incoming_data(type_of_message,data,time,lat,lot,speed,course,height, sats, hdops, inputs, outputs, adc, ibutton, params) values (%s, %s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s);', data)

        except con.Error as err:
            print('Error: ', err)
          
        else:
            print("Success")
            conn.commit()
        
    elif (len(calls) == 10):  #Short msg
        
        data.append(calls[0])
        data.append(calls[1])
        data.append(calls[2] + calls[3])
        data.append(calls[4] + calls[5])
        data.append(calls[6])
        data.append(calls[7])
        data.append(calls[8])
        data.append(calls[9])
        
        try:
            cursor.execute('INSERT into rango_incoming_data(type_of_message,data,time,lat,lot,speed,course,height, sats) values ("SD", %s,%s,%s,%s,%s,%s,%s,%s);', data)
            
        except con.Error as err:
            print('Error: ', err)
        else:
            print("Success")
            conn.commit()
        
    elif (len(calls) == 1):  #msg to server
        
        data.append(calls[0])
        
        try:
            cursor.execute('INSERT into rango_incoming_data(type_of_message,data) values ("M", %s);', data)

        except con.Error as err:
            print('Error: ', err)
        else:
            print("Success")
            conn.commit()
    
    return data

def check_p(message,imei='not-file'):

    str_data = []
    
    chto = message.split('#')[0]

    while (message.find(chto) == 0 and  message.find('\r\n')>0):
        start_D = message.find(chto)
        end_D = message.find('\r\n')

        data = decode(message[0:end_D+2])

        if (start_D == 0) and (end_D > 0):
          str_data.append(message[0:end_D+2])
          message = message[end_D+2:]

        else:
          break

    dict_return = {1:str_data,2:message}

    return dict_return

async def handle_echo(reader, writer):
    start_L = -1
    end_L   = -1
    message = ''
    imei=''
    while True:
        data = await reader.read(10000)
        message = message +  data.decode()
        if message == '': break
        addr = writer.get_extra_info('peername')

        if start_L < 0:
        # esho nikto ne loginilsa !ishem login
            start_L = message.find('#L#')
            end_L = message.find('\r\n')

            if (start_L == 0) and (end_L  > 0):
                str_login=message[0:end_L+2]
                imei=str_login[3:str_login.find(';')]
                #print_log(imei,"Received login %r imei %r" % (str_login, imei))
                message = message[end_L+2:]


                try:
                    cursor.execute('INSERT into rango_incoming_data(type_of_message,IMEI) values ("L",%s);', ([imei]))
                    #result = cursor.fetchall()
                except con.Error as err:
                    print('Error: ', err)
                    writer.write(b'#AL#0\r\n')
                    await writer.drain()
                else:
                    conn.commit()
                    writer.write(b'#AL#1\r\n')
                    await writer.drain()
#                print("Received login %r from %r" % (str_login, imei),file=log)
                

        dict_D = check_p(message,imei)
        list_D =   dict_D[2]
        message = dict_D[2]

#        for i in dict_D[1]:
#         print (i)

        writer.write(b'#AD#1\r\n')
        await writer.drain()

    print("Close the client socket")
    writer.close()

    
def main():    
    
    
    
    conn = con.connect(user = 'django', password = 'asd1', host = 'localhost', database = 'tango')
    cursor = conn.cursor()
    
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_echo, '85.12.197.205', 20332, loop=loop)
    server = loop.run_until_complete(coro)
    
    global is_server_up
    is_server_up = True

# Serve requests until Ctrl+C is pressed
    global a
    a = 'Serving on {}'.format(server.sockets[0].getsockname())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

def close_server():
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
    global is_server_up
    is_server_up = False
