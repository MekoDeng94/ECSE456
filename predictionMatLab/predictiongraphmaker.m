close all
clear
clc

data = csvread("prediction.csv",1,1);
date = readtable("date.csv");
dateX = table2array(date(622:682,:)); 

x = datenum(dateX);

subplot(2,1,1)
plot(x,data(622:682,1),'--ob',x,data(622:682,2),'-or')
datetick('x', 'yyyy-mm-dd')
title('Predicted')
ylabel('Normalized Mid Point Value')
xlabel('Date')
legend('Real Mid point value','Predicted Mid Point value');

% Calculate the correct direction percent
real = data(:,1);
diffReal = diff(real);
dirReal = sign(diffReal);
prediction = data(:,2);
diffPrediction = diff(prediction);
dirPrediction = sign(diffPrediction);
correctDirection = dirReal == dirPrediction;
percent = 100*sum(correctDirection==1) / size(correctDirection,1);
errorScore = sum(abs(diffReal-diffPrediction));

% Calculating the mean square error
err = immse(real,prediction);
subplot(2,1,2)
errVector = (real - prediction).^2;
h = histogram(errVector);
hold on
line([err,err],[0,max(h.Values)],'Color','Black')
hold off
h.BinWidth=err/50;
axis([0,0.10,0,max(h.Values)])
title('Histogram of squared error')
txt = ['\leftarrow Mean Squared Error: ' num2str(err) newline ...
    blanks(5) 'Correct direction: ' num2str(percent) '%' newline ...
    blanks(5) 'Error Score: ' num2str(errorScore)];
text(err,max(h.Values)/2,txt);