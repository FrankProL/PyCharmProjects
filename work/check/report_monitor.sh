#!/bin/bash
#Author:tiger.L

#set -ex

monitor_type=$1
current_time=$(date +'%Y/%m/%d %H:%M:%S')
echo "执行时间：${current_time},监控类型：${monitor_type}" >> /tmp/monitor.log

#根据监控类型，取得对应文件
if [ -z ${monitor_type} ];then
    send_flag=/tmp/send_flag
    result_file=/tmp/result
    monitor_log=/var/log/report_monitor.log
else
    send_flag=/tmp/send_flag_${monitor_type}
    result_file=/tmp/result_${monitor_type}
    if [ "${monitor_type}" == "file" ];then
        monitor_log=/var/log/monitor_file_hour.log    
    else
        monitor_log=/var/log/report_monitor_${monitor_type}.log
    fi
fi

#判断文件是否存在，不存在则创建
[ ! -e ${result_file} ] && touch ${result_file}
[ ! -e ${monitor_log} ] && echo "No monitor log file !" && exit 1
[ ! -e ${send_flag} ] && echo 0 > ${send_flag}

#进行过滤判断
if [ "${monitor_type}" == "file" ];then
    /bin/grep -v ',0$' ${monitor_log} >${result_file}
else
    /bin/grep ',0' ${monitor_log} |awk -F ',' '{print $1}' >${result_file}
fi


#输出结果集
flag=$(cat ${send_flag})
if [ -s ${result_file} ];then
    /bin/sed ':a;N;$!ba;s/\n/,/g' ${result_file}|cut -c 1-30
    if [ ${flag} -eq 0 ];then
        #/usr/local/bin/python /usr/local/zabbix/scripts/errorToEmail.py ${result_file}
        echo 1 > ${send_flag}
    fi
else
    echo "null"
    echo 0 > ${send_flag}
fi
