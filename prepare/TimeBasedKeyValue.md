# Time Based Key Value

https://www.youtube.com/watch?v=kZAZqn_J8Fo



```java
class TimeMap{
  	private Map<String, List<Data>> map;
  	
  	public TimeMap(){
      	map = new HashMap<>();
    }
  	
  	public set(String key, String value, int timestamp){
      	if(!HashMap.containsKey(key)) map.put(key, new ArrayList<>());
      	map.get(key).add(Data(value, timestamp));
    }
  	
  	public get(String key, int timestamp){
    		if (!map.containsKey(key)) return ""
        List<Data> data = map.get(key);
      	return findClosestValue(data, timestamp);
    }
  
  	public findClosestValue(List<Data> data, int timestamp){
        int l = 0, r = data.size() - 1;
        while(l < r){
          	int mid = (r + l + 1) / 2;
          	if (data.get(mid).timestamp < timestamp) l = mid;
          	else r = mid - 1;
        }
      	
      	Data closestData = data.get(l);
      	return cloestData.timestamp > timestamp ? "" : closestData.value
    }
  
		class Data{
        private String value;
        private int timestamp;

        public Data(String value, int timestamp){
            this.value = value;
            this.timestamp = timestamp;
        }
    }
}
```

