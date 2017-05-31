#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

ESP8266WebServer server(80);

int turns = 175;
String msgs = "E"; //------------------------------------------------------- Change Node here -----<

void setup() {
  // Let's initiate
  delay(100);
  // Set to STA+AP mode and disconnect from any previous connections
  WiFi.mode(WIFI_AP_STA);
  if (WiFi.status() == WL_CONNECTED) {WiFi.disconnect();}
  delay(100);
  // Create the access point
  WiFi.softAP("E"); //------------------------------------------------------ Change Node here -----<
  // Setup action upon client connection
  server.on("/", handleRoot); server.begin();
  delay(40000); //--------------------------------------------------------- Change Delay here -----<
}

void loop() {
  server.handleClient();
  // Run for only 175 times
  if (turns > 0) {
    // Initiate scan and let background tasks run
    WiFi.scanNetworks(true); yield(); delay(50);
    // Scan
    int n = WiFi.scanComplete();
    // If there are networks,
    if (n >= 0) {
      // Ignore the first 25 results
      if (turns < 150) {
        // Add a new line
        msgs += "\n";
        // Go thru each network to see if it's a node and if it's a node, add it to the msgs
        for (int i = 0; i < n; ++i) {
          if ((WiFi.SSID(i)).length() == 1) {
            msgs += WiFi.SSID(i); msgs += (":"); msgs += (WiFi.RSSI(i) * -1); msgs += (" ");
          }
        }
      }
      // When the scan is done, stop scanning
      --turns; WiFi.scanDelete();
    }
  }
}

void handleRoot() {
  server.send(200, "text/plain", msgs);
}
