import torch

class Stage2(torch.nn.Module):

    def __init__(self):
        super(Stage2, self).__init__()
        self.layer229 = torch.nn.ReLU(inplace=True)
        self.layer230 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer231 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer232 = torch.nn.ReLU(inplace=True)
        self.layer233 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer234 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer235 = torch.nn.ReLU(inplace=True)
        self.layer236 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer237 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer238 = torch.nn.ReLU(inplace=True)
        self.layer239 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer240 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer241 = torch.nn.ReLU(inplace=True)
        self.layer242 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer243 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer244 = torch.nn.ReLU(inplace=True)
        self.layer245 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer246 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer247 = torch.nn.ReLU(inplace=True)
        self.layer248 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer249 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer250 = torch.nn.ReLU(inplace=True)
        self.layer251 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer252 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer253 = torch.nn.ReLU(inplace=True)
        self.layer254 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer255 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer256 = torch.nn.ReLU(inplace=True)
        self.layer257 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer258 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer259 = torch.nn.ReLU(inplace=True)
        self.layer260 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer261 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer262 = torch.nn.ReLU(inplace=True)
        self.layer263 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer264 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer265 = torch.nn.ReLU(inplace=True)
        self.layer266 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer267 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer268 = torch.nn.ReLU(inplace=True)
        self.layer269 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer270 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer271 = torch.nn.ReLU(inplace=True)
        self.layer272 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer273 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer274 = torch.nn.ReLU(inplace=True)
        self.layer275 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer276 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer277 = torch.nn.ReLU(inplace=True)
        self.layer278 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer279 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer280 = torch.nn.ReLU(inplace=True)
        self.layer281 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer282 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer283 = torch.nn.ReLU(inplace=True)
        self.layer284 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer285 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer286 = torch.nn.ReLU(inplace=True)
        self.layer287 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer288 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer289 = torch.nn.ReLU(inplace=True)
        self.layer290 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer291 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer292 = torch.nn.ReLU(inplace=True)
        self.layer293 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer294 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer295 = torch.nn.ReLU(inplace=True)
        self.layer296 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer297 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer298 = torch.nn.ReLU(inplace=True)
        self.layer299 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer300 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer301 = torch.nn.ReLU(inplace=True)
        self.layer302 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer303 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer304 = torch.nn.ReLU(inplace=True)
        self.layer305 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer306 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer307 = torch.nn.ReLU(inplace=True)
        self.layer308 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer309 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer310 = torch.nn.ReLU(inplace=True)
        self.layer311 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer312 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer313 = torch.nn.ReLU(inplace=True)
        self.layer314 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer315 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer316 = torch.nn.ReLU(inplace=True)
        self.layer317 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer318 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer319 = torch.nn.ReLU(inplace=True)
        self.layer320 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer321 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer322 = torch.nn.ReLU(inplace=True)
        self.layer323 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer324 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer325 = torch.nn.ReLU(inplace=True)
        self.layer326 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer327 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer328 = torch.nn.ReLU(inplace=True)
        self.layer329 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer330 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer331 = torch.nn.ReLU(inplace=True)
        self.layer332 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer333 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer334 = torch.nn.ReLU(inplace=True)
        self.layer335 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer336 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer337 = torch.nn.ReLU(inplace=True)
        self.layer338 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer339 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer340 = torch.nn.ReLU(inplace=True)
        self.layer341 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer342 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self._initialize_weights()

    def forward(self, input0, input1):
        in0 = input0.clone()
        in1 = input1.clone()
        out226 = in0
        out228 = in1
        out229 = self.layer229(out228)
        out230 = self.layer230(out229)
        out231 = self.layer231(out230)
        out232 = self.layer232(out231)
        out233 = self.layer233(out232)
        out234 = self.layer234(out233)
        out234 = out226 + out234
        out235 = self.layer235(out234)
        out236 = self.layer236(out235)
        out237 = self.layer237(out236)
        out238 = self.layer238(out237)
        out239 = self.layer239(out238)
        out240 = self.layer240(out239)
        out241 = self.layer241(out240)
        out242 = self.layer242(out241)
        out243 = self.layer243(out242)
        out243 = out235 + out243
        out244 = self.layer244(out243)
        out245 = self.layer245(out244)
        out246 = self.layer246(out245)
        out247 = self.layer247(out246)
        out248 = self.layer248(out247)
        out249 = self.layer249(out248)
        out250 = self.layer250(out249)
        out251 = self.layer251(out250)
        out252 = self.layer252(out251)
        out252 = out244 + out252
        out253 = self.layer253(out252)
        out254 = self.layer254(out253)
        out255 = self.layer255(out254)
        out256 = self.layer256(out255)
        out257 = self.layer257(out256)
        out258 = self.layer258(out257)
        out259 = self.layer259(out258)
        out260 = self.layer260(out259)
        out261 = self.layer261(out260)
        out261 = out253 + out261
        out262 = self.layer262(out261)
        out263 = self.layer263(out262)
        out264 = self.layer264(out263)
        out265 = self.layer265(out264)
        out266 = self.layer266(out265)
        out267 = self.layer267(out266)
        out268 = self.layer268(out267)
        out269 = self.layer269(out268)
        out270 = self.layer270(out269)
        out270 = out262 + out270
        out271 = self.layer271(out270)
        out272 = self.layer272(out271)
        out273 = self.layer273(out272)
        out274 = self.layer274(out273)
        out275 = self.layer275(out274)
        out276 = self.layer276(out275)
        out277 = self.layer277(out276)
        out278 = self.layer278(out277)
        out279 = self.layer279(out278)
        out279 = out271 + out279
        out280 = self.layer280(out279)
        out281 = self.layer281(out280)
        out282 = self.layer282(out281)
        out283 = self.layer283(out282)
        out284 = self.layer284(out283)
        out285 = self.layer285(out284)
        out286 = self.layer286(out285)
        out287 = self.layer287(out286)
        out288 = self.layer288(out287)
        out288 = out280 + out288
        out289 = self.layer289(out288)
        out290 = self.layer290(out289)
        out291 = self.layer291(out290)
        out292 = self.layer292(out291)
        out293 = self.layer293(out292)
        out294 = self.layer294(out293)
        out295 = self.layer295(out294)
        out296 = self.layer296(out295)
        out297 = self.layer297(out296)
        out297 = out289 + out297
        out298 = self.layer298(out297)
        out299 = self.layer299(out298)
        out300 = self.layer300(out299)
        out301 = self.layer301(out300)
        out302 = self.layer302(out301)
        out303 = self.layer303(out302)
        out304 = self.layer304(out303)
        out305 = self.layer305(out304)
        out306 = self.layer306(out305)
        out306 = out298 + out306
        out307 = self.layer307(out306)
        out308 = self.layer308(out307)
        out309 = self.layer309(out308)
        out310 = self.layer310(out309)
        out311 = self.layer311(out310)
        out312 = self.layer312(out311)
        out313 = self.layer313(out312)
        out314 = self.layer314(out313)
        out315 = self.layer315(out314)
        out315 = out307 + out315
        out316 = self.layer316(out315)
        out317 = self.layer317(out316)
        out318 = self.layer318(out317)
        out319 = self.layer319(out318)
        out320 = self.layer320(out319)
        out321 = self.layer321(out320)
        out322 = self.layer322(out321)
        out323 = self.layer323(out322)
        out324 = self.layer324(out323)
        out324 = out316 + out324
        out325 = self.layer325(out324)
        out326 = self.layer326(out325)
        out327 = self.layer327(out326)
        out328 = self.layer328(out327)
        out329 = self.layer329(out328)
        out330 = self.layer330(out329)
        out331 = self.layer331(out330)
        out332 = self.layer332(out331)
        out333 = self.layer333(out332)
        out333 = out325 + out333
        out334 = self.layer334(out333)
        out335 = self.layer335(out334)
        out336 = self.layer336(out335)
        out337 = self.layer337(out336)
        out338 = self.layer338(out337)
        out339 = self.layer339(out338)
        out340 = self.layer340(out339)
        out341 = self.layer341(out340)
        out342 = self.layer342(out341)
        return (out334, out342)

    def _initialize_weights(self):
            for m in self.modules():
                if isinstance(m, torch.nn.Conv2d):
                    torch.nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                elif isinstance(m, torch.nn.BatchNorm2d):
                    torch.nn.init.constant_(m.weight, 1)
                    torch.nn.init.constant_(m.bias, 0)
