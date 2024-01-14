import torch

class Stage1(torch.nn.Module):

    def __init__(self):
        super(Stage1, self).__init__()
        self.layer115 = torch.nn.ReLU(inplace=True)
        self.layer116 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)  # 14
        self.layer117 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer118 = torch.nn.ReLU(inplace=True)
        self.layer119 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)  # 14
        self.layer120 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer121 = torch.nn.ReLU(inplace=True)
        self.layer122 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)  # 14
        self.layer123 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer124 = torch.nn.ReLU(inplace=True)
        self.layer125 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)  # 14
        self.layer126 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer127 = torch.nn.ReLU(inplace=True)
        self.layer128 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)  # 14
        self.layer129 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer130 = torch.nn.ReLU(inplace=True)
        self.layer131 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)  # 14
        self.layer132 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer133 = torch.nn.ReLU(inplace=True)
        self.layer134 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer135 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer136 = torch.nn.ReLU(inplace=True)
        self.layer137 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer138 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer139 = torch.nn.ReLU(inplace=True)
        self.layer140 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer141 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer142 = torch.nn.ReLU(inplace=True)
        self.layer143 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer144 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer145 = torch.nn.ReLU(inplace=True)
        self.layer146 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer147 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer148 = torch.nn.ReLU(inplace=True)
        self.layer149 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer150 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer151 = torch.nn.ReLU(inplace=True)
        self.layer152 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer153 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer154 = torch.nn.ReLU(inplace=True)
        self.layer155 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer156 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer157 = torch.nn.ReLU(inplace=True)
        self.layer158 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer159 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer160 = torch.nn.ReLU(inplace=True)
        self.layer161 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer162 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer163 = torch.nn.ReLU(inplace=True)
        self.layer164 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer165 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer166 = torch.nn.ReLU(inplace=True)
        self.layer167 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer168 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer169 = torch.nn.ReLU(inplace=True)
        self.layer170 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer171 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer172 = torch.nn.ReLU(inplace=True)
        self.layer173 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer174 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer175 = torch.nn.ReLU(inplace=True)
        self.layer176 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer177 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer178 = torch.nn.ReLU(inplace=True)
        self.layer179 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer180 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer181 = torch.nn.ReLU(inplace=True)
        self.layer182 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer183 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer184 = torch.nn.ReLU(inplace=True)
        self.layer185 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer186 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer187 = torch.nn.ReLU(inplace=True)
        self.layer188 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer189 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer190 = torch.nn.ReLU(inplace=True)
        self.layer191 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer192 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer193 = torch.nn.ReLU(inplace=True)
        self.layer194 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer195 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer196 = torch.nn.ReLU(inplace=True)
        self.layer197 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer198 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer199 = torch.nn.ReLU(inplace=True)
        self.layer200 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer201 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer202 = torch.nn.ReLU(inplace=True)
        self.layer203 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer204 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer205 = torch.nn.ReLU(inplace=True)
        self.layer206 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer207 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer208 = torch.nn.ReLU(inplace=True)
        self.layer209 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer210 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer211 = torch.nn.ReLU(inplace=True)
        self.layer212 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer213 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer214 = torch.nn.ReLU(inplace=True)
        self.layer215 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer216 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer217 = torch.nn.ReLU(inplace=True)
        self.layer218 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer219 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer220 = torch.nn.ReLU(inplace=True)
        self.layer221 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer222 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer223 = torch.nn.ReLU(inplace=True)
        self.layer224 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)  # 14
        self.layer225 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer226 = torch.nn.ReLU(inplace=True)
        self.layer227 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)  # 14
        self.layer228 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self._initialize_weights()

    def forward(self, input0, input1):
        in0 = input0.clone()
        in1 = input1.clone()
        out114 = in0 + in1
        out115 = self.layer115(out114)
        out116 = self.layer116(out115)
        out117 = self.layer117(out116)
        out118 = self.layer118(out117)
        out119 = self.layer119(out118)
        out120 = self.layer120(out119)
        out121 = self.layer121(out120)
        out122 = self.layer122(out121)
        out123 = self.layer123(out122)
        out123 = out115 + out123
        out124 = self.layer124(out123)
        out125 = self.layer125(out124)
        out126 = self.layer126(out125)
        out127 = self.layer127(out126)
        out128 = self.layer128(out127)
        out129 = self.layer129(out128)
        out130 = self.layer130(out129)
        out131 = self.layer131(out130)
        out132 = self.layer132(out131)
        out133 = self.layer133(out132)
        out134 = self.layer134(out133)
        out135 = self.layer135(out134)
        out135 = out124 + out135
        out136 = self.layer136(out135)
        out137 = self.layer137(out136)
        out138 = self.layer138(out137)
        out139 = self.layer139(out138)
        out140 = self.layer140(out139)
        out141 = self.layer141(out140)
        out142 = self.layer142(out141)
        out143 = self.layer143(out142)
        out144 = self.layer144(out143)
        out144 = out136 + out144
        out145 = self.layer145(out144)
        out146 = self.layer146(out145)
        out147 = self.layer147(out146)
        out148 = self.layer148(out147)
        out149 = self.layer149(out148)
        out150 = self.layer150(out149)
        out151 = self.layer151(out150)
        out152 = self.layer152(out151)
        out153 = self.layer153(out152)
        out153 = out145 + out153
        out154 = self.layer154(out153)
        out155 = self.layer155(out154)
        out156 = self.layer156(out155)
        out157 = self.layer157(out156)
        out158 = self.layer158(out157)
        out159 = self.layer159(out158)
        out160 = self.layer160(out159)
        out161 = self.layer161(out160)
        out162 = self.layer162(out161)
        out162 = out154 + out162
        out163 = self.layer163(out162)
        out164 = self.layer164(out163)
        out165 = self.layer165(out164)
        out166 = self.layer166(out165)
        out167 = self.layer167(out166)
        out168 = self.layer168(out167)
        out169 = self.layer169(out168)
        out170 = self.layer170(out169)
        out171 = self.layer171(out170)
        out171 = out163 + out171
        out172 = self.layer172(out171)
        out173 = self.layer173(out172)
        out174 = self.layer174(out173)
        out175 = self.layer175(out174)
        out176 = self.layer176(out175)
        out177 = self.layer177(out176)
        out178 = self.layer178(out177)
        out179 = self.layer179(out178)
        out180 = self.layer180(out179)
        out180 = out172 + out180
        out181 = self.layer181(out180)
        out182 = self.layer182(out181)
        out183 = self.layer183(out182)
        out184 = self.layer184(out183)
        out185 = self.layer185(out184)
        out186 = self.layer186(out185)
        out187 = self.layer187(out186)
        out188 = self.layer188(out187)
        out189 = self.layer189(out188)
        out189 = out181 + out189
        out190 = self.layer190(out189)
        out191 = self.layer191(out190)
        out192 = self.layer192(out191)
        out193 = self.layer193(out192)
        out194 = self.layer194(out193)
        out195 = self.layer195(out194)
        out196 = self.layer196(out195)
        out197 = self.layer197(out196)
        out198 = self.layer198(out197)
        out198 = out190 + out198
        out199 = self.layer199(out198)
        out200 = self.layer200(out199)
        out201 = self.layer201(out200)
        out202 = self.layer202(out201)
        out203 = self.layer203(out202)
        out204 = self.layer204(out203)
        out205 = self.layer205(out204)
        out206 = self.layer206(out205)
        out207 = self.layer207(out206)
        out207 = out198 + out207
        out208 = self.layer208(out207)
        out209 = self.layer209(out208)
        out210 = self.layer210(out209)
        out211 = self.layer211(out210)
        out212 = self.layer212(out211)
        out213 = self.layer213(out212)
        out214 = self.layer214(out213)
        out215 = self.layer215(out214)
        out216 = self.layer216(out215)
        out216 = out208 + out216
        out217 = self.layer217(out216)
        out218 = self.layer218(out217)
        out219 = self.layer219(out218)
        out220 = self.layer220(out219)
        out221 = self.layer221(out220)
        out222 = self.layer222(out221)
        out223 = self.layer223(out222)
        out224 = self.layer224(out223)
        out225 = self.layer225(out224)
        out225 = out217 + out225
        out226 = self.layer226(out225)
        out227 = self.layer227(out226)
        out228 = self.layer228(out227)
        return (out226, out228)

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, torch.nn.Conv2d):
                torch.nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, torch.nn.BatchNorm2d):
                torch.nn.init.constant_(m.weight, 1)
                torch.nn.init.constant_(m.bias, 0)

