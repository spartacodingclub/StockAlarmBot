importClass(org.jsoup.Jsoup);
importPackage(com.dtolabs.rundeck.core.utils.TextUtils);
const scriptName = "front";
/**
 * (string) room
 * (string) sender
 * (boolean) isGroupChat
 * (void) replier.reply(message)
 * (boolean) replier.reply(room, message, hideErrorToast = false) // 전송 성공시 true, 실패시 false 반환
 * (string) imageDB.getProfileBase64()
 * (string) packageName
 */
function response(room, msg, sender, isGroupChat, replier, imageDB, packageName) {
    //replier.reply("김진환","시작");  
    // let url="http://13.125.255.233:5000/nations/stocks/";
    let url = "http://13.125.255.233:5000/nations/";
    let addUrl = ""
    let outMsg ="";
    let stockName = null;
    let flag=0;


    let msgIndex = msg.indexOf("주가");
    if (msgIndex == 0) {
        msgIndex = msg.indexOf(" ");
        if (msgIndex == 2) {
            let str = msg.split(" ");
            let str1 = str[0];
            let str2 = str[1];
            let str3 = str[2];
            if (str3 == null || str3.equals("")) {
                if (str2)
                    stockName = str2;
                addUrl = addUrl + "stocks/" + stockName;
            }
        }
    }


    msgIndex = msg.indexOf("지수");
    let dirtyFlag = 0;
    if (msgIndex == 0) {
        for (let i = 2; i < 5; i++) {
            if (msg[i] == " " || msg[i])
                dirtyFlag += 1;
        }
        if (dirtyFlag == 0) {
            addUrl = "indices";
            flag=1;
        }
    }


    msgIndex = msg.indexOf("선물");
    dirtyFlag = 0;
    if (msgIndex == 0) {
        for (let i = 2; i < 5; i++) {
            if (msg[i] == " " || msg[i])
                dirtyFlag += 1;
        }
        if (dirtyFlag == 0) {
            addUrl = "future_indices";
            flag=2;
        }
    }


    if (!addUrl.equals("")) {
        url += addUrl;
        outMsg = Jsoup.connect(url).timeout(15000).ignoreContentType(true).get().text();
    }
   
   
   
    if (flag == 1){
      let split=outMsg.split(" ");
      outMsg="";
      for (let i=0 ; i < split.length ; i++){
        outMsg+=split[i];
        outMsg+=" "
        if(i==19)
          break;
        if(i%4==3)
          outMsg+="\n";
        }
    }
    
    replier.reply("김진환",outMsg);
}
