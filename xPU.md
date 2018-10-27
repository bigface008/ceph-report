# xPU
xPU泛指一系列名称以英文字母开头芯片。各家芯片公司为了打响自己产品的名号，常常选一个别人
还没用过的英文字母再加上“PU”来命名自己的产品。下面大致介绍一下各种PU的信息。对其中比较重要
的CPU会有一定展开。本文参考的文章有
[零基础看懂全球AI芯片：详解“xPU”](https://zhuanlan.zhihu.com/p/28325678)。

## APU
### Accelerated Processing Unit
是AMD的一个处理器种类。通过在一颗芯片上集成传统CPU和图形处理器GPU，就可以不需要北桥，灵
活地在CPU和GPU间分配任务。AMD将这种异构的处理器称为加速处理单元，APU。APU可以代替入门
级显卡，对于需要轻量图形运算的人群来说性价比较高，有不小的优势。缺点是内存，由于CPU、GP
U共用一块内存，会引起一系列问题。

## BPU
- Brain Processing Unit 地平线机器人公司的AI芯片。
- Biological Processing Unit 生物计算机。
- Bio-Recognition Processing Unit 生物特征识别处理器。
## CPU
CPU主要工作是调度，在机器学习所需要的运算模式下优势不大，因而缺点就是无法针对特定算法高效地进行优化。但这不意味着没有公司在使用CPU进行人工智能方面的工作。

首先，很多公司的AI处理器中还是会使用CPU做控制调度。
> 比如，wave computing用的是Andes的 CPU core；Mobileye用了好几个MIPS的CPU core；国内的某些AI芯片公司用的ARM的CPU core。此外，在现有的移动市场的AP中，在CPU之外，再集成一两个AI加速器IP（例如针对视觉应用的DSP，见VPU部分）也是一种趋势。例如，华为近期就在为其集成了AI加速器的麒麟970做宣传。

另外，做高性能计算CPU的公司也不甘错过AI的浪潮。例如：
- [Adapteva](http://www.adapteva.com/)。一家做多核MIMD结构处理器的公司。
- [kalrayinc](www.kalrayinc.com/)。一家做多核并行处理器的公司，有针对数据中心和自动驾
学习计算的协处理器。
- celerity。这不是公司，是今年hotchip上公布的一个学术项目，由多个大学的学生开发的，总开发时间才9个月。用的16nm工艺，面价5x5，集成了511个RISC-V core，以及一个可以跑到625MHz的BNN（binarized neural network）加速器。
## DPU
D是Deep Learning的首字母，以Deep Learning开头来命名AI芯片是一种很自然的思路。实际上能用来做深度学习的处理器差不多都能叫这名字。
### Deep-Learning Processing Unit
深度学习处理器。DPU并不是哪家公司的专属术语。在学术圈，Deep Learning Processing Unit（或processor）被经常提及。例如ISSCC 2017新增的一个session的主题就是Deep Learning Processor。
### Deep Learning Accelerator
深度学习加速器。NVIDA的重量级开源项目，目前已经有相当多有关的实践项目。

## GPU
### Graphics Processing Unit
图形处理器。GPU原来最大的需求来自PC市场上各类游戏对图形处理的需求。但是随着移动设备的升级，在移动端也逐渐发展起来。GPU在人工智能、挖矿、游戏领域都是炙手可热的存在。很难说它有什么明显的缺点。相关的公司有：

- NVIDIA。说起GPU，毫无疑问现在的老大是NVIDIA。这家成立于1993年的芯片公司一直致力于设计各种GPU：针对个人和游戏玩家的GeForce系列，针对专业工作站的Quadro系列，以及针对服务器和高性能运算的Tesla系列。随着AI的发展，NVIDIA在AI应用方面不断发力，推出了针对自动驾驶的DRIVE系列，以及专为AI打造的VOLTA架构。

- AMD。AMD新出的MI系列GPU将目标对准AI。

在移动端市场，GPU被三家公司瓜分，但是也阻止不了新的竞争者杀入。

- ARM家的Mali。来自于ARM于2006年收购的Falanx公司。Falanx最初的GPU是面向PC市场的，但是根本就无法参与到NVIDIA和ATI的竞争中去，于是转向移动市场。
- Imagination的PowerVR。主要客户是苹果，所以主要精力都在支持苹果，对其他客户的支持不足。但是，苹果突然宣布放弃PVR转为自研，对Imagination打击不小，股价大跌六成。Imagination现在正在寻求整体出售。
- Qualcomm的Adreno。
- VeriSilicon的Vivante。Vivante（图芯）是一家成立于2004年的以做嵌入式GPU为主的芯片公司，于2015年被VSI收购。Vivante的市场占有率较低。
- Samsung的。。。哦，三星没有自己的GPU。作为一个IDM巨头，对于没有自家的GPU，三星一直耿耿于怀。三星也宣布要研发自家的移动端GPU芯片，不过要等到2020年了。
- Apple。Apple在最新的产品发布会上，宣布A11中集成了其自己设计的GPU，要比A10性能提高30%，但是只需要一半的功耗。

## HPU
### Holographic Processing Unit
全息处理器。Microsoft专为自家Hololens应用开发的。第一代HPU采用28nm HPC工艺，使用了24个Tensilica DSP并进行了定制化扩展。HPU支持5路cameras、1路深度传感器（Depth sensor）和1路动作传感器（Motion Sensor）。Microsoft 在最近的CVPR 2017上宣布了HPU2的一些信息。HPU2将搭载一颗支持DNN的协处理器，专门用于在本地运行各种深度学习。指的一提的是，HPU是一款为特定应用所打造的芯片，这个做产品的思路可以学习。据说Microsoft评测过Movidius（见VPU部分）的芯片，但是觉得无法满足算法对性能、功耗和延迟的要求，所有才有了HPU。

## IPU
### Intelligence Processing Unit
智能处理器。以IPU命名芯片的有两家公司。

- Graphcore。Graphcore公司的IPU是专门针对graph的计算而打造的。稍微说说Graph，Graphcore认为Graph是知识模型及相应算法的非常自然的表示，所以将Graph作为机器智能的基础表示方法，既适用于神经网络，也适用于贝叶斯网络和马尔科夫场，以及未来可能出现的新的模型和算法。Graphcore的IPU一直比较神秘，直到近期才有一些细节的信息发布。比如：16nm，同构多核（>1000）架构，同时支持training和inference，使用大量片上sram，性能优于Volta GPU和TPU2，预计2017年底会有产品发布，等等。多八卦一点，Graphcore的CEO和CTO以前创立的做无线通信芯片的公司Icera于2011年被Nvidia收购并于2015年关闭。关于IPU更细节的描述，可以看唐博士的微信公号的一篇文章，传输门：解密又一个xPU：Graphcore的IPU。

- Mythic。另外一家刚融了$9.3 million的start-up公司Mythic也提到了IPU：“Mythic's intelligence processing unit (IPU) adds best-in-class intelligence to any device”。和现在流行的数字电路平台方案相比，Mythic号称可以将功耗降到1/50。之所以这么有信心，是因为他们使用的“processing in memory”结构。关于Processing in Memory，又可以大写一篇了，这里就不扩展了。有兴趣的，可以google一下“UCSB 谢源”，从他的研究开始了解。

- Image Cognition Processor
图像认知处理器ICP，加拿大公司CogniVue开发的用于视觉处理和图像认知的IP。

- Image Processing Unit
图像处理器。一些SOC芯片中将处理静态图像的模块称为IPU。但是，IPU不是一个常用的缩写，更常见的处理图像信号的处理器的缩写为下面的ISP。

> google的新发布的pixel 2手机中，集成了一颗自己设计的芯片，pixel visual core。从其公布的layout看，内部集成了8个图像处理单元IPU，每个IPU包含512个ALU。算力达到3Tflops（对比华为NPU 1.92Tflops，苹果Neural Engine 0.6Tflops）。与第一代pixel手机比，在visual core的支持下，HDR+计算的速度提升了5倍，功耗却只有1/10。这就是硬件加速的收益。

- Image Signal Processor 图像信号处理器。

## NPU
### Neural-Network Processing Unit
与GPU类似，神经网络处理器NPU已经成为了一个通用名词，而非某家公司的专用缩写。由于神经网络计算的类型和计算量与传统计算的区别，导致在进行NN计算的时候，传统CPU、DSP甚至GPU都有算力、性能、能效等方面的不足，所以激发了专为NN计算而设计NPU的需求。这里罗列几个以NPU名义发布过产品的公司，以及几个学术圈的神经网络加速器。

- 中星微电子（Vimicro）的星光智能一号。

- Kneron。这是一家位于San Diego的start-up公司，针对IOT应用领域做deep learning IP开发。

- VeriSilicon（芯原）的VIP8000。创立于2001年。

- 杭州国芯的gxNPU。

- 华为&海思。市场期待华为的麒麟970已经很长时间了，内置的AI加速器被华为称为NPU。已经证实，就是使用了寒武纪的IP。算力是1.92Tflops，实测执行VGG-16模型，麒麟970的性能可以到300 GOPS。业界认定，华为下一代的NN加速器，会用自家开发的IP。并且，各路信息显示，海思的确在专门招纳相关人才。据传，海思的HI3559中使用的就是自己研发的深度学习加速器。

### Neural/Neuromorphic Processing Unit
神经/神经形态处理器。这和上面的神经网络处理器还有所不同。而且，一般也不以“处理器”的名字出现，更多的时候被称为“神经形态芯片（Neuromorphic Chip）”或者是“类脑芯片（Brain-Inspired Chip）”。这类AI芯片不是用CNN、DNN等网络形式来做计算，而是以更类似于脑神经组成结构的SNN（Spiking Neural Network）的形式来进行计算。随便列几个，都不是“xPU”的命名方式。

- Qualcomm的Zeroth。高通几年前将Zeroth定义为一款NPU，配合以软件，可以方便的实现SNN的计算。但是，NPU似乎不见了踪影，现在只剩下了同名的机器学习引擎Zeroth SDK。
- IBM的TrueNorth。
- Intel的Loihi。
- BrainChip的SNAP（Spiking Neuron Adaptive Processor ）。
- GeneralVision的CM1K、NM500 chip，以及NeuroMem IP。
- Knowm。
- Koniku。
- westwell。
- Neural Network Accelerator。

## RPU
### Ray-tracing Processing Unit
光线追踪处理器。Ray tracing是计算机图形学中的一种渲染算法，RPU是为加速其中的数据计算而开发的加速器。现在这些计算都是GPU的事情了。

## SPU
### Streaming Processing Unit
流处理器。流处理器的概念比较早了，是用于处理视频数据流的单元，一开始出现在显卡芯片的结构里。可以说，GPU就是一种流处理器。

### Speech-Recognition Processing Unit
语音识别处理器，SPU或SRPU。这个缩写还没有公司拿来使用。现在的语音识别和语义理解主要是在云端实现的，比如科大讯飞。

## TPU
### Tensor Processing Unit
Google的张量处理器。2016年AlphaGo打败李世石，2017年AlphaGo打败柯洁，两次人工智能催化事件给芯片行业带来的冲击无疑就是TPU的出现和解密。Google在2017年5月的开发者I/O大会上正式公布了TPU2，又称Cloud TPU。相比于TPU1，TPU2既可以用于training，又可以用于inference。TPU1使用了脉动阵列的流处理结构，具体的细节可以参考如下的文章“Google TPU 揭密”。可以说是人工智能芯片的头牌。

## VPU
### Vision Processing Unit
视觉处理器VPU也有希望成为通用名词。作为现今最火热的AI应用领域，计算机视觉的发展的确能给用户带来前所未有的体验。为了处理计算机视觉应用中遇到的超大计算量，多家公司正在为此设计专门的VPU。包括：
- Movidius（已被Intel收购）。
- Inuitive。
- DeepVision。

### Vector Processing Unit
向量处理器。标量处理器、向量处理器、张量处理器，这是以处理器处理的数据类型进行的划分。现在的CPU已经不再是单纯的标量处理器，很多CPU都集成了向量指令，最典型的就是SIMD。向量处理器在超级计算机和高性能计算中，扮演着重要角色。基于向量处理器研发AI领域的专用芯片，也是很多公司的选项。例如，前面刚提到Movidius的Myriad2中，就包含了12个向量处理器。

### Vision DSP
针对AI中的计算机视觉应用，各家DSP公司都发布了DSP的Vision系列IP。简单罗列如下。

- CEVA的XM4，最新的XM6 DSP。
- Tensilica（2013年被Cadence以3.8亿美元收购）的P5、P6，以及最新的C5 DSP。
- Synopsys的EV5x和EV6x系列DSP。
- Videantis的v-MP4系列。

## Others
### 寒武纪科技（Cambricon）
寒武纪没有用xPU的方式命名自家的处理器。媒体的文章既有称之为深度学习处理器DPU的，也有称之为神经网络处理器NPU的。寒武纪Cambricon-X指令集是其一大特色。目前其芯片IP已扩大范围授权集成到手机、安防、可穿戴设备等终端芯片中。在一些特殊领域，寒武纪的芯片将在国内具有绝对的占有率。

### Intel
Intel在数据中心/云计算方面，167亿美金收购的Altera，4亿美金收购Nervana；在移动端的无人机、安防监控等方面收购Movidius；在ADAS方面收购Mobileye。大概是在智能手机上吃的亏让它非常后悔吧。

### 苹果
苹果正在研发一款AI芯片，内部称为“苹果神经引擎”(Apple Neural Engine)。
### 高通
高通除了维护其基于Zeroth的软件平台，在硬件上也动作不断。收购NXP的同时，据传高通也一直在和Yann LeCun以及Facebook的AI团队保持合作，共同开发用于实时推理的新型芯片。