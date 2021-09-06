import redis
import pandas as pd
import pickle
import time
import logging
import os

class Redis():
    '''
        This class is to confiugre redis infomation and provide get and set data
    '''
    logger = logging.getLogger("garage")

    def __init__(self, host, port, pw):
        self.update_redis(host,port,pw)
        self.redis_conn = redis.StrictRedis(host=self.redis_host, port=self.redis_port, db=0)
        #self.redis_conn = redis.StrictRedis(host=self.redis_host, port=self.redis_port, db=0, password=self.redis_pw)

    def update_redis(self, host,port,pw):
        self.redis_host = host
        self.redis_port = port
        self.redis_pw = pw

    def check_exists_key(self, key):
        return self.redis_conn.exists(key)

    def set_data(self, data, key):
        '''
        This funciton is for setting data to redis
            
        Parameters
            data(dataFrame) : The sql reulst data to save to redis
            key(str) : the unique key name to distinguish from other data

        Returns
           True/Flase(boolean):
               If there is the same key in redis,
            it will return false otherwise it will return ture 

        '''
        new_data = pickle.dumps(data)
        self.redis_conn.set(key, new_data, ex=500)
        self.logger.info("success")

    def get_data(self, key):
        '''
        This funciton is for getting data from redis
            
        Parameters
            key(str) : the unique key name to find

        Returns
           data(DataFrame) which is saved in redis

        '''
        data = self.redis_conn.get(key)
        return pickle.loads(data)
 