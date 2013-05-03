int truePositives = c_TruePosi;
int falsePositives = c_FalsePos;
int trueNegatives = c_TrueNega;
int falseNegatives = c_FalseNeg;
int total = truePositives + falsePositives + trueNegatives + falseNegatives; 


double accuracy = ((double)truePositives + trueNegatives) /total;
double specificity = (double)trueNegatives / (trueNegatives + falsePositives);
double sensitivity = (double)truePositives / (truePositives + falseNegatives);
double balancedAccuracy = (specificity + sensitivity)/2;

double top = (((double)truePositives * trueNegatives) - (falsePositives * falseNegatives));
double bottom = Math.sqrt(((double)truePositives + falsePositives) * (truePositives + falseNegatives) * (trueNegatives + falsePositives) * (trueNegatives + falseNegatives));
double mcc = top / bottom;

double precision = (double)truePositives / (truePositives + falsePositives);
double falsePositiveRate = (((double)falsePositives) / (falsePositives + trueNegatives));

out_Accura = accuracy;
out_Specif = specificity;
out_Sensit = sensitivity;
out_Balanc = balancedAccuracy;
out_MCC = mcc;
out_Precis = precision;
out_FalseP = falsePositiveRate;
