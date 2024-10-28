## AMI-Br: A Dataset of Typical and Atypical Mitotic Figures on Human Breast Cancer}

This repository provides the AMI-Br dataset, a subclassification of all mitotic figures (MFs) in the TUPAC16 and MIDOG21 datasets into phases of the mitotic cycle and into atypical morphologies.

The dataset is stored in the CSV file and contains the following information:
- slide : file name of the original image
- dataset : MIDOG21 (2021 edition of MIDOG) and TUPAC16 (from tupac.grand-challenge.org)
- uid : uid within the original dataset
- x,y : coordinates on the original image
- expert1_label, expert2_label: 8-class subclassification by two experts (see below)
- expert1_atypical, expert2_atypical, expert3_atypical: binary classification by three experts into normal and atypical mitotic figures. Is True in case of atypical MF.
- majority_atypical: Indication if majority of experts (previous three columns) found this MF to be an atypical MF.

We futhermore provide crop-outs (128x128 px) of the agreed atypical and normal MF in the folder `patches`.

We used the relabeled version of the TUPAC16 dataset, which has an overall higher consistency:
```
Bertram, C. A., Veta, M., Marzahl, C., Stathonikos, N., Maier, A., Klopfleisch, R., & Aubreville, M. (2020). Are pathologist-defined labels reproducible? Comparison of the TUPAC16 mitotic figure dataset with an alternative set of labels. In Interpretable and Annotation-Efficient Learning for Medical Image Computing: Third International Workshop, iMIMIC 2020, Second International Workshop, MIL3ID 2020, and 5th International Workshop, LABELS 2020, Held in Conjunction with MICCAI 2020, Lima, Peru, October 4–8, 2020, Proceedings 3 (pp. 204-213). Springer International Publishing.
```
