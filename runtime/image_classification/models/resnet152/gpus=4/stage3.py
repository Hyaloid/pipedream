import torch

class Stage3(torch.nn.Module):

    def __init__(self):
        super(Stage3, self).__init__()
        self.layer343 = torch.nn.ReLU(inplace=True)
        self.layer344 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer345 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer346 = torch.nn.ReLU(inplace=True)
        self.layer347 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer348 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer349 = torch.nn.ReLU(inplace=True)
        self.layer350 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer351 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer352 = torch.nn.ReLU(inplace=True)
        self.layer353 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer354 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer355 = torch.nn.ReLU(inplace=True)
        self.layer356 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer357 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer358 = torch.nn.ReLU(inplace=True)
        self.layer359 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer360 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer361 = torch.nn.ReLU(inplace=True)
        self.layer362 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer363 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer364 = torch.nn.ReLU(inplace=True)
        self.layer365 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer366 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer367 = torch.nn.ReLU(inplace=True)
        self.layer368 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer369 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer370 = torch.nn.ReLU(inplace=True)
        self.layer371 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer372 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer373 = torch.nn.ReLU(inplace=True)
        self.layer374 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer375 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer376 = torch.nn.ReLU(inplace=True)
        self.layer377 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer378 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer379 = torch.nn.ReLU(inplace=True)
        self.layer380 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer381 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer382 = torch.nn.ReLU(inplace=True)
        self.layer383 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer384 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer385 = torch.nn.ReLU(inplace=True)
        self.layer386 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer387 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer388 = torch.nn.ReLU(inplace=True)
        self.layer389 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer390 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer391 = torch.nn.ReLU(inplace=True)
        self.layer392 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer393 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer394 = torch.nn.ReLU(inplace=True)
        self.layer395 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer396 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer397 = torch.nn.ReLU(inplace=True)
        self.layer398 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer399 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer400 = torch.nn.ReLU(inplace=True)
        self.layer401 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer402 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer403 = torch.nn.ReLU(inplace=True)
        self.layer404 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer405 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer406 = torch.nn.ReLU(inplace=True)
        self.layer407 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer408 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer409 = torch.nn.ReLU(inplace=True)
        self.layer410 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer411 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer412 = torch.nn.ReLU(inplace=True)
        self.layer413 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer414 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer415 = torch.nn.ReLU(inplace=True)
        self.layer416 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer417 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer418 = torch.nn.ReLU(inplace=True)
        self.layer419 = torch.nn.Conv2d(1024, 256, kernel_size=(1, 1), stride=(1, 1), bias=False)#14
        self.layer420 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer421 = torch.nn.ReLU(inplace=True)
        self.layer422 = torch.nn.Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)#14
        self.layer423 = torch.nn.BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer424 = torch.nn.ReLU(inplace=True)
        self.layer425 = torch.nn.Conv2d(256, 1024, kernel_size=(1, 1), bias=False)#14
        self.layer426 = torch.nn.BatchNorm2d(1024, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer427 = torch.nn.ReLU(inplace=True)

        self.layer428 = torch.nn.Conv2d(1024, 512, kernel_size=(1, 1), stride=(2, 2), bias=False)
        self.layer429 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer430 = torch.nn.ReLU(inplace=True)
        self.layer431 = torch.nn.Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        self.layer432 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer433 = torch.nn.ReLU(inplace=True)
        self.layer434 = torch.nn.Conv2d(512, 2048, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layer435 = torch.nn.BatchNorm2d(2048, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer436 = torch.nn.ReLU(inplace=True)
        self.layer437 = torch.nn.Conv2d(2048, 512, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layer438 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer439 = torch.nn.ReLU(inplace=True)
        self.layer440 = torch.nn.Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        self.layer441 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer442 = torch.nn.ReLU(inplace=True)
        self.layer443 = torch.nn.Conv2d(512, 2048, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layer444 = torch.nn.BatchNorm2d(2048, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer445 = torch.nn.ReLU(inplace=True)
        self.layer446 = torch.nn.Conv2d(2048, 512, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layer447 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer448 = torch.nn.ReLU(inplace=True)
        self.layer449 = torch.nn.Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        self.layer450 = torch.nn.BatchNorm2d(512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer451 = torch.nn.ReLU(inplace=True)
        self.layer452 = torch.nn.Conv2d(512, 2048, kernel_size=(1, 1), stride=(1, 1), bias=False)
        self.layer453 = torch.nn.BatchNorm2d(2048, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.layer454 = torch.nn.ReLU(inplace=True)

        self.layer455 = torch.nn.AvgPool2d(kernel_size=7, stride=1, padding=0)
        self.layer456 = torch.nn.Linear(in_features=2048, out_features=1000, bias=True)
        self._initialize_weights()

    def forward(self, input0, input1):
        in0 = input0.clone()
        in1 = input1.clone()
        out342 = in0 + in1
        out343 = self.layer343(out342)
        out344 = self.layer344(out343)
        out345 = self.layer345(out344)
        out346 = self.layer346(out345)
        out347 = self.layer347(out346)
        out348 = self.layer348(out347)
        out349 = self.layer349(out348)
        out350 = self.layer350(out349)
        out351 = self.layer351(out350)
        out351 = out343 + out351
        out352 = self.layer352(out351)
        out353 = self.layer353(out352)
        out354 = self.layer354(out353)
        out355 = self.layer355(out354)
        out356 = self.layer356(out355)
        out357 = self.layer357(out356)
        out358 = self.layer358(out357)
        out359 = self.layer359(out358)
        out360 = self.layer360(out359)
        out360 = out352 + out360
        out361 = self.layer361(out360)
        out362 = self.layer362(out361)
        out363 = self.layer363(out362)
        out364 = self.layer364(out363)
        out365 = self.layer365(out364)
        out366 = self.layer366(out365)
        out367 = self.layer367(out366)
        out368 = self.layer368(out367)
        out369 = self.layer369(out368)
        out369 = out361 + out369
        out370 = self.layer370(out369)
        out371 = self.layer371(out370)
        out372 = self.layer372(out371)
        out373 = self.layer373(out372)
        out374 = self.layer374(out373)
        out375 = self.layer375(out374)
        out376 = self.layer376(out375)
        out377 = self.layer377(out376)
        out378 = self.layer378(out377)
        out378 = out370 + out378
        out379 = self.layer379(out378)
        out380 = self.layer380(out379)
        out381 = self.layer381(out380)
        out382 = self.layer382(out381)
        out383 = self.layer383(out382)
        out384 = self.layer384(out383)
        out385 = self.layer385(out384)
        out386 = self.layer386(out385)
        out387 = self.layer387(out386)
        out387 = out379 + out387
        out388 = self.layer388(out387)
        out389 = self.layer389(out388)
        out390 = self.layer390(out389)
        out391 = self.layer391(out390)
        out392 = self.layer392(out391)
        out393 = self.layer393(out392)
        out394 = self.layer394(out393)
        out395 = self.layer395(out394)
        out396 = self.layer396(out395)
        out396 = out388 + out396
        out397 = self.layer397(out396)
        out398 = self.layer398(out397)
        out399 = self.layer399(out398)
        out400 = self.layer400(out399)
        out401 = self.layer401(out400)
        out402 = self.layer402(out401)
        out403 = self.layer403(out402)
        out404 = self.layer404(out403)
        out405 = self.layer405(out404)
        out405 = out397 + out405
        out406 = self.layer406(out405)
        out407 = self.layer407(out406)
        out408 = self.layer408(out407)
        out409 = self.layer409(out408)
        out410 = self.layer410(out409)
        out411 = self.layer411(out410)
        out412 = self.layer412(out411)
        out413 = self.layer413(out412)
        out414 = self.layer414(out413)
        out414 = out406 + out414
        out415 = self.layer415(out414)
        out416 = self.layer416(out415)
        out417 = self.layer417(out416)
        out418 = self.layer418(out417)
        out419 = self.layer419(out418)
        out420 = self.layer420(out419)
        out421 = self.layer421(out420)
        out422 = self.layer422(out421)
        out423 = self.layer423(out422)
        out423 = out415 + out423
        out424 = self.layer424(out423)
        out425 = self.layer425(out424)
        out426 = self.layer426(out425)
        out427 = self.layer427(out426)
        out428 = self.layer428(out427)
        out429 = self.layer429(out428)
        out430 = self.layer430(out429)
        out431 = self.layer431(out430)
        out432 = self.layer432(out431)
        out433 = self.layer433(out432)
        out434 = self.layer434(out433)
        out435 = self.layer435(out434)
        out436 = self.layer436(out435)
        out437 = self.layer437(out436)
        out438 = self.layer438(out437)
        out439 = self.layer439(out438)
        out440 = self.layer440(out439)
        out441 = self.layer441(out440)
        out441 = out429 + out441
        out442 = self.layer442(out441)
        out443 = self.layer443(out442)
        out444 = self.layer444(out443)
        out445 = self.layer445(out444)
        out446 = self.layer446(out445)
        out447 = self.layer447(out446)
        out448 = self.layer448(out447)
        out449 = self.layer449(out448)
        out450 = self.layer450(out449)
        out451 = self.layer451(out450)
        out452 = self.layer452(out451)
        out453 = self.layer453(out452)
        out454 = self.layer454(out453)
        out455 = self.layer455(out454)
        out456 = out455.size(0)
        out457 = out455.view(out456, -1)
        out458 = self.layer456(out457)
        return out458

    def _initialize_weights(self):
            for m in self.modules():
                if isinstance(m, torch.nn.Conv2d):
                    torch.nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                elif isinstance(m, torch.nn.BatchNorm2d):
                    torch.nn.init.constant_(m.weight, 1)
                    torch.nn.init.constant_(m.bias, 0)
