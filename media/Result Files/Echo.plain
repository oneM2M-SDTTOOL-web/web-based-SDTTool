# Domain "example.based.on.echonetLite"

> 

 

## ModuleClasses
### operationStatus






#### Data Points

|Name |Type |R/W |Optional |Unit |Documentation |
|:----|:----|:---|:--------|:----|:-------------|
| operationStatus | boolean  | R/W | false |  | This property indicates the ON/OFF status. |


 ### installationLocation






#### Data Points

|Name |Type |R/W |Optional |Unit |Documentation |
|:----|:----|:---|:--------|:----|:-------------|
| installationLocation | string  | R/W | false |  | This property indicates the installation location |

#### Events

|Name |Data |Optional |Documentation |
|:----|:----|:--------|:-------------|
| installationLocation |  | None |  |


 ### measuredInstantaneousPowerConsumption






#### Data Points

|Name |Type |R/W |Optional |Unit |Documentation |
|:----|:----|:---|:--------|:----|:-------------|
| measuredInstantaneousPowerConsumption | integer  | R | false | watts | This property indicates the instantaneous power consumption of the device in watts. |


 ### temperatureSensorDataPoints






#### Data Points

|Name |Type |R/W |Optional |Unit |Documentation |
|:----|:----|:---|:--------|:----|:-------------|
| measuredTemperatureValue | integer  | R | false | celsius | This property indicates the measured temperature value in units of 0.1C. |


   

## DeviceClasses
### SimpleWaschingMachine


#### Properties

|Name |Type |Value |Optional |Documentation |
|:----|:----|:-----|:--------|:-------------|
| Name | string | washing machine | false |  |
| Vendor | string | ACME | false |  |
#### Extended ModuleClasses

|ModuleClass Instance Name |ModuleClass Name |Cardinality |Description |
|:-------------------------|:----------------|:-----------|:-----------|
|installationLocation | example.based.on.echonetLite : installationLocation | 1 |  |
 |measuredInstantaneousPowerConsumption | example.based.on.echonetLite : measuredInstantaneousPowerConsumption | 1 |  |
 |temperatureSensorDataPoints | example.based.on.echonetLite : temperatureSensorDataPoints | 1 |  |
 |washingMachineOperationStatus | example.based.on.echonetLite : operationStatus | 1 |  |
    
#### ModuleClasses
##### washingMachineDataPoints



- **Cardinality**: 1



###### Data Points

|Name |Type |R/W |Optional |Unit |Documentation |
|:----|:----|:---|:--------|:----|:-------------|
| door_CoverOpen_CloseStatus | boolean  | R | false |  | This property indicates whether the door/cover is open or closed. |
| washingMachineSetting | string  | R/W | false |  | Washing machine setting |
| currentStageOfWashingCycle | string  | R | false |  | This property indicates the current stage of the washing cycle. |
| timeRemainingToCompleteWashingCycle | time  | R | false |  | This property indicates the time remaining to complete the current washing cycle in the HH:MM:SS format. |
| onTimerReservationSetting | boolean  | R/W | false |  | Reservation ON/OFF |
| onTimerSetting | time  | R/W | false |  | Timer value (HH:MM) |
| relativeTimeBasedOnTimerSetting | time  | R/W | false |  | Timer value (HH:MM) |


   




