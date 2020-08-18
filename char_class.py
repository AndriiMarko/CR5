import pygame

CHAR_IMG_WIDTH = 2400
CHAR_IMG_HEIGHTT = 1300

LAYER_TAIL = 0
LAYER_HAIRBACK = 1
LAYER_HAIRRIGHTTAIL = 2
LAYER_LEGS = 3
LAYER_WINGS = 4
LAYER_HEADTORSO = 5
LAYER_RIGHTARM = 6
LAYER_HAIRMIDDLE = 7
LAYER_HAIRLEFTTAIL = 8
LAYER_LEFTARM = 9
LAYER_BOOBS = 10
LAYER_EARS = 11
LAYER_EYESPUPILS = 12
LAYER_EYES = 13
LAYER_MIMIC = 14
LAYER_HAIRFRONT = 15
LAYER_HORNS = 16
LAYERS_BODY_NUM = 17

COLOR_TYPE_NONE = 0
COLOR_TYPE_HORN = 1
COLOR_TYPE_EYE = 2
COLOR_TYPE_EYE2 = 3
COLOR_TYPE_HAIR = 4
COLOR_TYPE_HAIR2 = 5
COLOR_TYPE_SKIN = 6
COLOR_TYPE_SKIN2 = 7
COLOR_TYPE_TAIL1 = 8
COLOR_TYPE_TAIL2 = 9
COLOR_TYPE_WINGS1 = 10
COLOR_TYPE_WINGS2 = 11
        

AP_TAIL_NONE = ('none', 0)
AP_TAIL_FOXTAIL = ('FoxTail2', pygame.Color(255, 103, 11), pygame.Color(255, 255, 255))
AP_TAIL_CATTAIL = ('CatTail', pygame.Color(110, 164, 214))
AP_TAILS = (AP_TAIL_NONE, AP_TAIL_FOXTAIL, AP_TAIL_CATTAIL)

AP_WINGS_BATWINGS = ('BatWings2', 0, 0)

AP_HAIRBACK_NONE = ('none', 0)
AP_HAIRBACK_LONG = ('LongHairBack', pygame.Color(241, 235, 189), 0)
AP_HAIRBACK_LONGSTRAIGHT = ('LongStraightHairBack', pygame.Color(241, 235, 189), 0)
AP_HAIRBACKS = (AP_HAIRBACK_NONE, AP_HAIRBACK_LONG, AP_HAIRBACK_LONGSTRAIGHT)

AP_HAIRRIGHTTAIL_NONE = ('none', 0)
AP_HAIRRIGHTTAIL_LONGTAIL =  ('LongTailRightHairTail', pygame.Color(241, 235, 189), 0)
AP_HAIRRIGHTTAIL_SHORTTAIL =  ('ShortTailRightHairTail', pygame.Color(241, 235, 189), 0)
AP_HAIRRIGHTTAILS = (AP_HAIRRIGHTTAIL_NONE, AP_HAIRRIGHTTAIL_LONGTAIL, AP_HAIRRIGHTTAIL_SHORTTAIL)

AP_HEADTORSO_HUMAN = ('HumanBody', 0, 0)
AP_LEGS_HUMAN = ('HumanLegs2', 0, 0)
AP_RIGHTARM_HUMAN = ('HumanRightArm2', 0, 0)

AP_HAIRMIDDLE_NONE = ('none', 0)
AP_HAIRMIDDLE_CARE = ('CareHairMiddle', pygame.Color(241, 235, 189), 0)
AP_HAIRMIDDLE_LONGSTRAIGHT = ('LongStraightHairMiddle', pygame.Color(241, 235, 189), 0)
AP_HAIRMIDDLE_LONG = ('LongHairMiddle', pygame.Color(241, 235, 189), 0)
AP_HAIRMIDDLES = (AP_HAIRMIDDLE_NONE, AP_HAIRMIDDLE_CARE, AP_HAIRMIDDLE_LONGSTRAIGHT, AP_HAIRMIDDLE_LONG)

AP_HAIRLEFTTAIL_NONE = ('none', 0)
AP_HAIRLEFTTAIL_LONGTAIL =  ('LongTailHairLeftTail', pygame.Color(241, 235, 189), 0)
AP_HAIRLEFTTAIL_SHORTTAIL =  ('ShortTailHairLeftTail', pygame.Color(241, 235, 189), 0)
AP_HAIRLEFTTAILS = (AP_HAIRLEFTTAIL_NONE, AP_HAIRLEFTTAIL_LONGTAIL, AP_HAIRLEFTTAIL_SHORTTAIL)

AP_LEFTARM_HUMAN = ('HumanLeftArm2', 0, 0)
AP_BOOBS_2 = ('2Boobs2', 0, 0)
AP_EERS_HUMAN = ('HumanEars2', 0, 0)
AP_EYESPUPILS_1 = ('Pupils1', 0, 0)
AP_EYES_1 = ('Eyes1', 0, 0)
AP_MIMIC_NORMAL = ('NormalMimic1', 0, 0)
AP_HAIRFRONT_CARE = ('CareHairFront', pygame.Color(241, 235, 189), 0)
AP_HORNS_1 = ('Horns1', 0, 0)

def img_merge(img_list):
    merged_img = img_list[0].copy()
    #merged_img = pygame.Surface((img_list[0].get_width(), img_list[0].get_height()))
    #merged_img.fill((255, 255, 255))
    #merged_img.set_colorkey((255, 255, 255))
    #merged_img = img_list[0]
    #for img in img_list[1:]:
    for img in img_list[1:]:
        merged_img.blit(img, (0,0))
    return merged_img
    
def change_img_color (img, old_color, new_color):
    if (old_color == 0) or (new_color == 0):
        return img
    else:
        for x in range(img.get_width()):
            for y in range(img.get_height()):
                if img.get_at((x, y)) ==  old_color:
                    img.set_at((x,y), new_color)
        return img

def change_img_color2 (img, old_color, new_color):
    if not(len(old_color)==2):
        return img
    if not(len(new_color)==2):
        return img
    if (old_color[0] == 0) or (old_color[1] == 0) or (new_color[0] == 0) or (new_color[1] == 0):
        return img
    else:
        for x in range(img.get_width()):
            for y in range(img.get_height()):
                if img.get_at((x, y)) ==  old_color[0]:
                    img.set_at((x,y), new_color[0])
                elif img.get_at((x, y)) ==  old_color[1]:
                    img.set_at((x,y), new_color[1])
        return img

def load_leyer( img_path, img, new_color=[]):
    try:
        img_surf = pygame.image.load(img_path + img[0]+".png")
    except pygame.error:
        print ('img download fail '+ img_path + img[0])
    
    if (len(img) == 3):
        if len(new_color) == 2:
            #if (type(img[1]) ==  type(pygame.Color())) and (type(img[2]) ==  type(pygame.Color()))     and (type(new_color[0]) ==  type(pygame.Color())) and (type(new_color[1]) ==  type(pygame.Color())) :
            if (img[2] == 0) or (new_color[1] == 0):
                img_surf = change_img_color(img_surf, img[1], new_color[0])
            elif (img[1] == 0) or (new_color[0] == 0):
                img_surf = change_img_color(img_surf, img[2], new_color[1])
            else:
                img_surf = change_img_color2(img_surf, img[1:], new_color)
        elif len(new_color) == 1:
            img_surf = change_img_color(img_surf, img[1], new_color[0])
            #if (type(img[1]) ==  type(pygame.Color()))     and (type(new_color[0]) ==  type(pygame.Color())):
            
    elif (len(img) == 2):
        if len(new_color) >= 1:
            #if (type(img[1]) ==  type(pygame.Color()))  and (type(new_color[0]) ==  type(pygame.Color())):
                    img_surf = change_img_color(img_surf, img[1], new_color[0])
   
    return img_surf
                            
    
class Stats():
    def __init__(self):
        #base
        self.strenght = 0
        self.reflex = 0
        self.intelligence = 0
        self.luck = 0
        #second
        self.speed = 0
        self.fly_speed = 0
        self.teleport = 0
        self.perception = 0.0
        self.stealth = 0.0
        self.max_HP = 0
        self.max_MP = 0
        self.max_stamina = 0
        self.max_cast = 0
        #resist
        self.resist_dmg = Dmg_Types()
            
    def strenght_change(self, num):
        self.strenght += num
        #self.speed += num/4
        self.max_HP += num*2
        self.max_stamina += num*3
    
    def reflex_change(self, num):
        self.reflex += num
        #self.speed += num/4
        self.stealth += num/4
        
    def intelligence_change(self, num):
        self.intelligence += num
        self.perception += num/2
        self.stealth += num/4
        self.max_MP += num*2
            

        
class Char_Stats():
    def __init__(self):
        self.stats = Stats()
        self.stats.strenght = 10.0
        self.stats.reflex = 10.0
        self.stats.intelligence = 10.0
        self.stats.luck = 0
        self.stats.speed = 3
        self.stats.fly_speed = 0
        self.stats.teleport = 0
        self.stats.perception = self.stats.intelligence/2
        self.stats.stealth = (self.stats.intelligence +  self.stats.reflex)/4
        self.stats.max_HP = self.stats.strenght*2
        self.stats.max_MP = self.stats.intelligence*2
        self.stats.max_stamina = self.stats.strenght*3
        self.stats.max_cast = 0
        
        
        self.stats_bonuse = Stats()
        
        #current
        self.HP = self.stats.max_HP
        self.MP = self.stats.max_MP
        self.stamina = self.stats.max_stamina
        self.cast = self.stats.max_cast
        
            
        #exp
        self.lvl = 0
        self.exp = 0
        self.stat_points = 0
        self.skill_points = 0
        
        
class Magik_Skils():
    def __init__(self): 
        #element chaos-----------------------------
        #light
        self.light_lv = 0
        #lightning
        self.lightning_lv = 0
        #fire
        self.fire_lv = 0
        #wind
        self.wind_lv = 0
        
        #entrophy chaos-------------------------------------
        #life
        self.life_lv = 0
        #space
        self.space_lv = 0
        #power
        self.power_lv = 0
        #body
        self.body_lv = 0
        
        #element control-------------------------------------
        #dark
        self.dark_lv = 0
        #water
        self.water_lv = 0
        #ice
        self.ice_lv = 0
        #stone
        self.stone_lv = 0
        
        #entrophy control----------------------------------
        #deth
        self.deth_lv = 0
        #time
        self.time_lv = 0
        #vector
        self.vector_lv = 0
        #mind
        self.mind_lv = 0
        
class Weapon_Skils():
    def __init__(self): 
        #defensive-----------------------------------------
        self.defensive_lv = 0
        #long range--------------------------------------------
        #bow
        self.bow_lv = 0
        #throwing
        self.throwing_lv = 0
        
        #close range-------------------------------------------
        #blades
        self.piersing_blades_lv = 0
        self.cuting_blades_lv = 0
        self.choping_blades_lv = 0
        #pole
        self.piersing_pole_lv = 0
        self.cuting_pole_lv = 0
        self.choping_pole_lv = 0
        #flexible   
        self.piersing_flexible_lv = 0
        self.cuting_flexible_lv = 0
        self.choping_flexible_lv = 0    

class Cybernetic_Modifications():
    def __init__(self):
        #internal--------------------------------------
        self.interface = 0      
        self.motion_controller = 0
        self.gumoral_reg = 0
        self.eyes = 0
        self.ears = 0
        self.nose = 0
        self.radio = 0
        self.voise = 0
        self.eating_filtre = 0
        self.breathe_filtre = 0
        self.hart = 0
        self.skelet = 0
        self.blod_nanobots = 0
        self.skin = 0
        self.sensors = 0
        
        self.musculs = 0
        self.conectors = 0
        self.hand_weaponns = 0
        self.hand = 0
        self.electrick_shock = 0
        
        self.legs = 0
        self.foot = 0
        
        #external--------------------------------------
        self.manipulators = 0
        self.visor = 0
        self.anten = 0
        self.sholder_wepons = 0
        self.flying = 0
        self.side_mounted_wepon1 = 0
        self.side_mounted_wepon2 = 0

class Mutations():
    def __init__(self):
        self.ears = 0
        self.nose = 0
        self.lungs = 0
        self.tail = 0
        
        self.claws = 0
        self.poison_claws = 0
        self.electric_claws = 0
        
        self.legs = 0
        self.eyes = 0
        
        self.canine = 0
        self.poison_canine = 0
        self.chemical_canine = 0
        self.fire_canine = 0
        self.cold_canine = 0
        
        self.extra_hands_wings = 0
        self.bust = 0
        self.side_line = 0
        self.electrick = 0
        self.photosyntes = 0
        self.skin = 0
        self.horns = 0
        
class Cleric_Skils():
    def __init__(self):
        #good
        self.good_single_lv = 0
        self.good_poli_lv = 0
        self.good_spirit_lv = 0
        #neutral
        self.neutral_single_lv = 0
        self.neutral_poli_lv = 0
        self.neutral_spirit_lv = 0
        #evil
        self.evil_single_lv = 0
        self.evil_poli_lv = 0
        self.evil_spirit_lv = 0
        
        
class Hand_To_Hand_Skils():
    def __init__(self):
        #punch
        self.hand_punch = 0
        self.elbow_punch = 0
        self.foot_punch = 0
        self.knee_punch = 0
        #lock
        self.pain_lock = 0
        self.sufocation_lock = 0
        self.throw_lock = 0
    
class Gun_Skils():
    def __init__(self):
        self.old_gun_lv = 0
        self.revolver_lv = 0
        self.pistol_lv = 0
        self.SMG_lv = 0
        self.rifle_lv = 0
        self.AR_lv = 0
        self.shotgun_lv = 0
        self.MG_lv = 0
        self.granede_lv = 0
        self.rocket_lv = 0
        self.flame_thrower_lv = 0
        self.future_lv = 0
        
class Dmg_Types():
    def __init__(self):
        self.shock = 0
        self.pierse = 0
        self.fire = 0
        self.cold = 0
        self.radiation = 0
        self.chemical = 0
        self.necro = 0

class Status_Effects():
    def __init__(self):
        self.bleed = 0
        self.unconclusion = 0
        self.blind = 0
        self.cant_hear = 0
        self.lay_down = 0
        self.unbalance = 0
        self.burning = 0
        self.soaked = 0
        self.poison = 0

class Armor():
    def __init__(self):
        #dmg resist
        self.resist_dmg = Dmg_Types()
                
        self.dmg_throught_armor_pc = 0
        
        #effects resist
        self.resist_effects = Status_Effects()
    
                    
class Character_Appearance():
    def __init__(self):
        #color
        self.horns_color = 0
        self.eye_color = 0 #default
        self.eye_color2 = 0 #default
        self.hair_color = 0 #pygame.Color(189, 234, 241) #default
        self.hair_color2 = 0 #pygame.Color(242, 165, 228) #default
        self.skin_color =  0 #pygame.Color(247, 225, 198) #default
        self.skin_color2 = 0 #pygame.Color(255, 255, 255)
        self.tail_color1 = 0 #pygame.Color(101, 224, 124)
        self.tail_color2 = 0 #pygame.Color(189, 165, 212)
        self.wings_color1 = 0 #pygame.Color(255, 255, 255)
        self.wings_color2 = 0 #pygame.Color(242, 165, 228)
        #other
        self.body_type = 1
        self.height = 1
        
        self.cloac = ''
        self.drone = ''
        
        #body
        self.tail = AP_TAIL_FOXTAIL
        self.wings = AP_WINGS_BATWINGS
        self.hair_back = AP_HAIRBACK_LONG
        self.hair_right_tails = AP_HAIRRIGHTTAIL_LONGTAIL
        self.head_torso = AP_HEADTORSO_HUMAN
        self.legs = AP_LEGS_HUMAN
        self.right_arm = AP_RIGHTARM_HUMAN
        self.hair_middle = AP_HAIRMIDDLE_CARE
        self.hair_left_tails = AP_HAIRLEFTTAIL_LONGTAIL
        self.left_arm = AP_LEFTARM_HUMAN
        self.boobs = AP_BOOBS_2
        self.ears = AP_EERS_HUMAN
        self.eyes_pupils = AP_EYESPUPILS_1
        self.eyes = AP_EYES_1
        self.mimic = AP_MIMIC_NORMAL
        self.hair_front  = AP_HAIRFRONT_CARE
        self.horns = AP_HORNS_1
        
        #close
        self.penty = ''
        self.bra = ''
        self.stocking = ''
    
    def draw_char(self):
        #merge_img = pygame.Surface((4800, 3600)) 
        merge_img = pygame.Surface((2400, 1300))
        merge_img.set_colorkey((0, 0, 0))
        
        for layer_number in range(0, LAYERS_BODY_NUM):
            
            if layer_number == LAYER_TAIL:
                if self.tail[0]:
                    src_img = load_leyer("img/char/Tails/", self.tail, (self.tail_color1, self.tail_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_WINGS :        
                if self.wings[0]:
                    src_img = load_leyer("img/char/Wings/", self.wings, (self.wings_color1, self.wings_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_HAIRBACK :     
                if self.hair_back[0]:
                    src_img = load_leyer("img/char/HairBack/", self.hair_back, (self.hair_color, self.hair_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_HAIRRIGHTTAIL:
                if self.hair_right_tails[0]:
                    src_img = load_leyer("img/char/HairRightTails/", self.hair_right_tails, (self.hair_color, self.hair_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_HEADTORSO: 
                if self.head_torso[0]:
                    src_img = load_leyer("img/char/HeadTorso/", self.head_torso, (self.skin_color, self.skin_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_LEGS:          
                if self.legs[0]:
                    src_img = load_leyer("img/char/Legs/", self.legs, (self.skin_color, self.skin_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_RIGHTARM:              
                if self.right_arm[0]:
                    src_img = load_leyer("img/char/RightArm/", self.right_arm, (self.skin_color, self.skin_color2))
                    merge_img.blit(src_img, (0,0))
                
            if layer_number == LAYER_HAIRMIDDLE:    
                if self.hair_middle[0]:
                    src_img = load_leyer("img/char/HairMiddle/", self.hair_middle, (self.hair_color, self.hair_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_HAIRLEFTTAIL:                  
                if self.hair_left_tails[0]:
                    src_img = load_leyer("img/char/HairLeftTails/", self.hair_left_tails, (self.hair_color, self.hair_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_LEFTARM:                   
                if self.left_arm[0]:
                    src_img = load_leyer("img/char/LeftArm/", self.left_arm, (self.skin_color, self.skin_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_BOOBS: 
                if self.boobs[0]:
                    src_img = load_leyer("img/char/Boobs/", self.boobs, (self.skin_color, self.skin_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_EARS:                  
                if self.ears[0]:
                    src_img = load_leyer("img/char/Ears/", self.ears, (self.skin_color, self.skin_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_EYESPUPILS:                
                if self.eyes_pupils[0]: 
                    src_img = load_leyer("img/char/EyesPupils/", self.eyes_pupils, (self.eye_color, self.eye_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_EYES:  
                if self.eyes[0]:
                    src_img = load_leyer("img/char/Eyes/", self.eyes, (self.skin_color, self.skin_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_MIMIC:                 
                if self.mimic[0]:
                    src_img = load_leyer("img/char/Mimic/", self.mimic, (self.hair_color, self.hair_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_HAIRFRONT: 
                if self.hair_front[0]:
                    src_img = load_leyer("img/char/HairFront/", self.hair_front, (self.hair_color, self.hair_color2))
                    merge_img.blit(src_img, (0,0))
            
            if layer_number == LAYER_HORNS:                                 
                if self.horns[0]:
                    src_img = load_leyer("img/char/Horns/", self.horns, (self.hair_color, self.hair_color2))
                    merge_img.blit(src_img, (0,0))
            
        return merge_img
        
    def load_all_body_img(self, img_list):
        for layer_number in range(0, LAYERS_BODY_NUM):
            
            if layer_number == LAYER_TAIL:        
                if self.tail[0]:
                    img_list.append( load_leyer("img/char/Tails/", self.tail, (self.tail_color1, self.tail_color2)))
            
            elif layer_number == LAYER_WINGS:         
                if self.wings[0]:
                    img_list.append( load_leyer("img/char/Wings/", self.wings, (self.wings_color1, self.wings_color2)))
            
            elif layer_number == LAYER_HAIRBACK:          
                if self.hair_back[0]:
                    img_list.append( load_leyer("img/char/HairBack/", self.hair_back, (self.hair_color, self.hair_color2)))

            elif layer_number == LAYER_HAIRRIGHTTAIL:
                if self.hair_right_tails[0]:
                    img_list.append(  load_leyer("img/char/HairRightTails/", self.hair_right_tails, (self.hair_color, self.hair_color2)))
            
            elif layer_number == LAYER_HEADTORSO:     
                if self.head_torso[0]:
                    img_list.append(  load_leyer("img/char/HeadTorso/", self.head_torso, (self.skin_color, self.skin_color2)))
            
            elif layer_number == LAYER_LEGS:              
                if self.legs[0]:
                    img_list.append(  load_leyer("img/char/Legs/", self.legs, (self.skin_color, self.skin_color2)))
            
            elif layer_number == LAYER_RIGHTARM:                   
                if self.right_arm[0]:
                    img_list.append(  load_leyer("img/char/RightArm/", self.right_arm, (self.skin_color, self.skin_color2)))
            
            elif layer_number == LAYER_HAIRMIDDLE:       
                if self.hair_middle[0]:
                    img_list.append(  load_leyer("img/char/HairMiddle/", self.hair_middle, (self.hair_color, self.hair_color2)))
            
            elif layer_number == LAYER_HAIRLEFTTAIL:                      
                if self.hair_left_tails[0]:
                    img_list.append(  load_leyer("img/char/HairLeftTails/", self.hair_left_tails, (self.hair_color, self.hair_color2)))
            
            elif layer_number == LAYER_LEFTARM:                       
                if self.left_arm[0]:
                    img_list.append( load_leyer("img/char/LeftArm/", self.left_arm, (self.skin_color, self.skin_color2)))
            
            elif layer_number == LAYER_BOOBS:     
                if self.boobs[0]:
                    img_list.append( load_leyer("img/char/Boobs/", self.boobs, (self.skin_color, self.skin_color2)))
            
            elif layer_number == LAYER_EARS:                      
                if self.ears[0]:
                    img_list.append( load_leyer("img/char/Ears/", self.ears, (self.skin_color, self.skin_color2)))
            
            elif layer_number == LAYER_EYESPUPILS:                    
                if self.eyes_pupils[0]: 
                    img_list.append( load_leyer("img/char/EyesPupils/", self.eyes_pupils, (self.eye_color, self.eye_color2)))
            
            elif layer_number == LAYER_EYES:      
                if self.eyes[0]:
                    img_list.append( load_leyer("img/char/Eyes/", self.eyes, (self.skin_color, self.skin_color2)))
            
            elif layer_number == LAYER_MIMIC:                     
                if self.mimic[0]:
                    img_list.append(  load_leyer("img/char/Mimic/", self.mimic, (self.hair_color, self.hair_color2)))
            
            elif layer_number == LAYER_HAIRFRONT:      
                if self.hair_front[0]:
                     img_list.append(  load_leyer("img/char/HairFront/", self.hair_front, (self.hair_color, self.hair_color2)))
            
            elif layer_number == LAYER_HORNS:                                     
                if self.horns[0]:
                    img_list.append( load_leyer("img/char/Horns/", self.horns, (self.hair_color, self.hair_color2)))
               
        return img_list
        
    def load_all_body_img_resized(self, img_list, resolution): 
        for layer_number in range(0, LAYERS_BODY_NUM):
            
            if layer_number == LAYER_TAIL:
                if self.tail[0]:
                    img = load_leyer("img/char/Tails/", self.tail, (self.tail_color1, self.tail_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_WINGS:         
                if self.wings[0]:
                    img = load_leyer("img/char/Wings/", self.wings, (self.wings_color1, self.wings_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_HAIRBACK:          
                if self.hair_back[0]:
                    img = load_leyer("img/char/HairBack/", self.hair_back, (self.hair_color, self.hair_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_HAIRRIGHTTAIL:
                if self.hair_right_tails[0]:
                    img = load_leyer("img/char/HairRightTails/", self.hair_right_tails, (self.hair_color, self.hair_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_HEADTORSO:     
                if self.head_torso[0]:
                    img = load_leyer("img/char/HeadTorso/", self.head_torso, (self.skin_color, self.skin_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_LEGS:              
                if self.legs[0]:
                    img = load_leyer("img/char/Legs/", self.legs, (self.skin_color, self.skin_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_RIGHTARM:                   
                if self.right_arm[0]:
                    img = load_leyer("img/char/RightArm/", self.right_arm, (self.skin_color, self.skin_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_HAIRMIDDLE:       
                if self.hair_middle[0]:
                    img = load_leyer("img/char/HairMiddle/", self.hair_middle, (self.hair_color, self.hair_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_HAIRLEFTTAIL:                      
                if self.hair_left_tails[0]:
                    img = load_leyer("img/char/HairLeftTails/", self.hair_left_tails, (self.hair_color, self.hair_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_LEFTARM:                       
                if self.left_arm[0]:
                    img = load_leyer("img/char/LeftArm/", self.left_arm, (self.skin_color, self.skin_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_BOOBS:     
                if self.boobs[0]:
                    img = load_leyer("img/char/Boobs/", self.boobs, (self.skin_color, self.skin_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_EARS:                      
                if self.ears[0]:
                    img = load_leyer("img/char/Ears/", self.ears, (self.skin_color, self.skin_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_EYESPUPILS:                    
                if self.eyes_pupils[0]: 
                    img = load_leyer("img/char/EyesPupils/", self.eyes_pupils, (self.eye_color, self.eye_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_EYES:      
                if self.eyes[0]:
                    img = load_leyer("img/char/Eyes/", self.eyes, (self.skin_color, self.skin_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_MIMIC:                     
                if self.mimic[0]:
                    img = load_leyer("img/char/Mimic/", self.mimic, (self.hair_color, self.hair_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_HAIRFRONT:      
                if self.hair_front[0]:
                    img = load_leyer("img/char/HairFront/", self.hair_front, (self.hair_color, self.hair_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
            
            elif layer_number == LAYER_HORNS:                                     
                if self.horns[0]:
                    img = load_leyer("img/char/Horns/", self.horns, (self.hair_color, self.hair_color2))
                    img_list.append(pygame.transform.scale(img, resolution))
               
        return img_list
    
    def reload_img_in_list(self, img_list, layer):
        if (layer == LAYER_TAIL) and (len(img_list)>LAYER_TAIL):
            if self.tail[0]:
                img = load_leyer("img/char/Tails/", self.tail, (self.tail_color1, self.tail_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
                
        if (layer == LAYER_WINGS) and (len(img_list)>LAYER_WINGS):        
            if self.wings[0]:
                img = load_leyer("img/char/Wings/", self.wings, (self.wings_color1, self.wings_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))

        if (layer == LAYER_HAIRBACK) and (len(img_list)>LAYER_HAIRBACK):         
            if self.hair_back[0]:
                img = load_leyer("img/char/HairBack/", self.hair_back, (self.hair_color, self.hair_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
                
        if (layer == LAYER_HAIRRIGHTTAIL) and (len(img_list)>LAYER_HAIRRIGHTTAIL): 
            if self.hair_right_tails[0]:
                img = load_leyer("img/char/HairRightTails/", self.hair_right_tails, (self.hair_color, self.hair_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
            
        if (layer == LAYER_HEADTORSO) and (len(img_list)>LAYER_HEADTORSO):     
            if self.head_torso[0]:
                img = load_leyer("img/char/HeadTorso/", self.head_torso, (self.skin_color, self.skin_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
            
        if (layer == LAYER_LEGS) and (len(img_list)>LAYER_LEGS):             
            if self.legs[0]:
                img = load_leyer("img/char/Legs/", self.legs, (self.skin_color, self.skin_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
            
        if (layer == LAYER_RIGHTARM) and (len(img_list)>LAYER_RIGHTARM):                  
            if self.right_arm[0]:
                img = load_leyer("img/char/RightArm/", self.right_arm, (self.skin_color, self.skin_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
            
        if (layer == LAYER_HAIRMIDDLE) and (len(img_list)>LAYER_HAIRMIDDLE):    
            if self.hair_middle[0]:
                img = load_leyer("img/char/HairMiddle/", self.hair_middle, (self.hair_color, self.hair_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
           
        if (layer == LAYER_HAIRLEFTTAIL) and (len(img_list)>LAYER_HAIRLEFTTAIL):                     
            if self.hair_left_tails[0]:
                img = load_leyer("img/char/HairLeftTails/", self.hair_left_tails, (self.hair_color, self.hair_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
           
        if (layer == LAYER_LEFTARM) and (len(img_list)>LAYER_LEFTARM):                     
            if self.left_arm[0]:
                img = load_leyer("img/char/LeftArm/", self.left_arm, (self.skin_color, self.skin_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
            
        if (layer == LAYER_BOOBS) and (len(img_list)>LAYER_BOOBS):     
            if self.boobs[0]:
                img = load_leyer("img/char/Boobs/", self.boobs, (self.skin_color, self.skin_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
          
        if (layer == LAYER_EARS) and (len(img_list)>LAYER_EARS):                     
            if self.ears[0]:
                img = load_leyer("img/char/Ears/", self.ears, (self.skin_color, self.skin_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
          
        if (layer == LAYER_EYESPUPILS) and (len(img_list)>LAYER_EYESPUPILS):                 
            if self.eyes_pupils[0]: 
                img = load_leyer("img/char/EyesPupils/", self.eyes_pupils, (self.eye_color, self.eye_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))

        if (layer == LAYER_EYES) and (len(img_list)>LAYER_EYES):     
            if self.eyes[0]:
                img = load_leyer("img/char/Eyes/", self.eyes, (self.skin_color, self.skin_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
          
        if (layer == LAYER_MIMIC) and (len(img_list)>LAYER_MIMIC):                     
            if self.mimic[0]:
                img = load_leyer("img/char/Mimic/", self.mimic, (self.hair_color, self.hair_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
           
        if (layer == LAYER_HAIRFRONT) and (len(img_list)>LAYER_HAIRFRONT):      
            if self.hair_front[0]:
                img = load_leyer("img/char/HairFront/", self.hair_front, (self.hair_color, self.hair_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))

        if (layer == LAYER_HORNS) and (len(img_list)>LAYER_HORNS):                                     
            if self.horns[0]:
                img = load_leyer("img/char/Horns/", self.horns, (self.hair_color, self.hair_color2))
                img_list[layer] = pygame.transform.scale(img, (img_list[layer].get_width(), img_list[layer].get_height()))
           
            
class Character():
    def __init__(self, name):
        self.name = name.title()
        self.sex = 'female' #?+
        self.apearence = Character_Appearance()
        self.race = "HUMAN"
        self.curse = ''
        self.age = 18
        self.temper = 'HERO'
        self.char_stats = Char_Stats()
    
        
        #skils
        self.magik_skils = Magik_Skils()
        self.weapon_skils = Weapon_Skils()
        self.cybernetical_modifications = Cybernetic_Modifications()
        self.mutations = Mutations()
        self.cleric_skils = Cleric_Skils()
        self.hand_to_hand_skils = Hand_To_Hand_Skils()
        self.guns_skil = Gun_Skils()
        
        self.money = 0
        #equip
        #self.head_Armor = Armor()
        #self.head_Torso = Armor()
        #self.head_LArm = Armor()
        #self.head_RArm = Armor()
        #self.head_LLeg = Armor()
        #self.head_RLeg = Armor()
        
        #weapon
        #self.weapon1
        #self.weapon2
        #self.weapon3
        #self.weapon4
        #inventory
        
    def Set_Race(self, race):
        self.race = race
        #humanoids
        if self.race == 'HUMAN':
            self.char_stats.stats.intelligence_change(1) 
            self.char_stats.stats.max_stamina += 3
            #APEARENCE
            self.apearence.hight = 168
        elif self.race == 'ORC':
            self.char_stats.stats.intelligence_change (-1)
            self.char_stats.stats.strenght_change(2)
            self.char_stats.stats.max_HP += 2
            #APEARENCE
            self.apearence.hight = 180
        elif self.race == 'HIGH_ELF':
            self.char_stats.stats.intelligence_change(2)
            self.char_stats.stats.max_MP += 2
            #APEARENCE
            self.apearence.hight = 160
        elif self.race == 'WOOD_ELF':
            self.char_stats.stats.reflex_change(2)
            self.char_stats.stats.speed += 1
            self.char_stats.stats.perception += 1
            self.char_stats.stats.stealth += 1
            #APEARENCE
            self.apearence.hight = 160
        elif self.race == 'DARK_ELF':
            self.char_stats.stats.reflex_change(2)
            self.char_stats.stats.perception += 2
            self.char_stats.stats.max_stamina += 1
            #APEARENCE
            self.apearence.hight = 160
        elif self.race == 'DWARF':
            self.char_stats.stats.strenght_change(1)
            self.char_stats.stats.speed -= 1
            self.char_stats.stats.max_HP += 2
            #APEARENCE
            self.apearence.hight = 150
        elif self.race == 'DERGAR':
            self.char_stats.stats.strenght_change(1)
            self.char_stats.stats.speed -= 1
            self.char_stats.stats.max_stamina += 3
            #APEARENCE
            self.apearence.hight = 150
        elif self.race == 'SWYRFNYBLEN':
            self.char_stats.stats.reflex_change(1)
            self.char_stats.stats.speed -= 1
            self.char_stats.stats.max_stamina += 3
            #APEARENCE
            self.apearence.hight = 130
        elif self.race == 'GNOME':
            self.char_stats.stats.intelligence_change(1)
            self.char_stats.stats.speed -= 1
            self.char_stats.stats.max_MP += 2
            #APEARENCE
            self.apearence.hight = 130
        elif self.race == 'GOBLIN':
            self.char_stats.stats.intelligence_change(-1)
            self.char_stats.stats.reflex_change(1)
            self.char_stats.stats.speed += 1
            self.char_stats.stats.perception += 1
            #APEARENCE
            self.apearence.hight = 130
        elif self.race == 'GREMLIN':
            self.char_stats.stats.reflex_change(1)
            self.char_stats.stats.perception += 1
            #APEARENCE
            self.apearence.hight = 130
        elif self.race == 'HOP_GOBLIN':
            self.char_stats.stats.strenght_change(1)
            self.char_stats.stats.speed += 1
            #APEARENCE
            self.apearence.hight = 150
        #Legendary
        #monster girl
        #elemental
        #automata
        
    def Set_Curse(self, curse):
        if not(self.race in RACE_AUTOMATA):
            self.curse = curse
            if self.curse == 'VAMPIRE':
                self.char_stats.stats.luck -=1
                self.char_stats.stats.reflex_change(1)
                self.char_stats.stats.resist_dmg.radiation -= 10
                self.char_stats.stats.resist_dmg.fire -= 5
                self.char_stats.stats.resist_dmg.necro += 100
                #APEARENCE
            elif self.curse == 'LICH':
                self.char_stats.stats.luck -=1
                self.char_stats.stats.resist_dmg.radiation -= 10
                self.char_stats.stats.resist_dmg.fire -= 5
                self.char_stats.stats.resist_dmg.cold += 5
                self.char_stats.stats.resist_dmg.necro += 100
                #APEARENCE
            elif self.curse == 'ZOMBIE':
                self.char_stats.stats.strenght_change(1)
                self.char_stats.stats.intelligence_change(-1)
                self.char_stats.stats.luck -=1
                self.char_stats.stats.resist_dmg.fire -= 10
                self.char_stats.stats.resist_dmg.necro += 100
                #APEARENCE
            elif self.curse == 'DALAHAN':
                self.char_stats.stats.luck -=1
                self.perception -= 1
                self.char_stats.stats.resist_dmg.fire -= 5
                self.char_stats.stats.resist_dmg.cold += 5
                self.char_stats.stats.resist_dmg.necro += 100
                #APEARENCE
            elif self.curse == 'GHOST':
                self.char_stats.stats.strenght_change(-2)
                self.char_stats.stats.reflex_change(-2)
                self.char_stats.stats.intelligence_change(-2)
                self.char_stats.stats.luck -=2
                self.char_stats.stats.resist_dmg.fire += 6
                self.char_stats.stats.resist_dmg.cold += 6
                self.char_stats.stats.resist_dmg.necro += 100
                self.char_stats.stats.resist_dmg.shock += 2
                self.char_stats.stats.resist_dmg.pierse += 4
                self.char_stats.stats.resist_dmg.chemical += 2
                #APEARENCE
            elif self.curse == 'WEREWOLF':
                self.char_stats.stats.luck -=1
                self.char_stats.stats.strenght_change(1)
                self.char_stats.stats.reflex_change(1)
                self.char_stats.stats.intelligence_change(-1)
                self.char_stats.stats.resist_dmg.fire -= 5
                #APEARENCE
            elif self.curse == 'POSESSED':
                self.char_stats.stats.intelligence_change(-1)
                self.char_stats.stats.luck -=1
                self.char_stats.stats.resist_dmg.fire += 5
                #APEARENCE
                
        
class Dmg_Skill():
    def __init__():
        #dmg
        self.dmg = Dmg_Types()
        
        
        self.dmg_throught_armor_pc = 0
        self.dmg_zone = 0
        #dmg deviation
        self.dmg_deviation = Dmg_Types()
        
        #effects
        self.effects = Status_Effects()
        

RACE_HUMANOIDS = ('ORC',    'HIGH_ELF', 'WOOD_ELF', 'DARK_ELF', 'HUMAN',
    'DWARF', 'DERGAR', 'SWYRFNYBLEN',   'GNOME', 'GOBLIN', 'GREMLIN',       
    'HOP_GOBLIN' )
RACE_LEGENDARY = ('ANGEL',  'SUCUBUS', 'GENIE', 'FAIRY',
    'DRYAD', 'PHENIX', 'DRAGON_BLUE', 'DRAGON_RED', 'DRAGON_GREEN', 
    'DRAGON_BLACK', 'DRAGON_WHITE', 'DRAGON_GOLD', 'DRAGON_SILVER',
     'DRAGON_BRONZE', 'DRAGON_CUPRUM', 'DRAGON_FERUM' )
RACE_MONSTERGIRLS = ('SLIME',   'HARPY',    'MERMAID',  'LAMIYA',   
    'CENTAUR',  'MINOTAUR', 'ARACHNA',  'CRAB', 'BEE',  'BUTTERFLY',
    'NECKOMIMI',    'INUMIMI',  'KITSUNEMIMI',  'UMAMIMI',  'USAGIMIMI',
    'NEZUMIMI', 'KUMAMIMI', 'NECKO_FURRY',      'INU_FURRY',    
    'KITSUNE_FURRY',    'UMA_FURRY',    'USAGI_FURRY',
    'NEZU_FURRY', 'KUMA_FURRY')
RACE_ELEMENTAL = ('LIGHTNING_EL',   'FIRE_EL',  'WIND_EL',  'WATER_EL',
    'ICE_EL',   'STONE_EL',     'LIGHT_EL', 'DARK_EL')
RACE_AUTOMATA = ('ANDROID', 'METAL_GOLEM',  'STONE_GOLEM',  'GARGOYLE')
RACE = (RACE_HUMANOIDS,  RACE_LEGENDARY, RACE_MONSTERGIRLS, 
    RACE_ELEMENTAL, RACE_AUTOMATA)

RACE_TYPES = ('RACE_HUMANOIDS',  'RACE_LEGENDARY', 'RACE_MONSTERGIRLS', 
    'RACE_ELEMENTAL', 'RACE_AUTOMATA')
    
CURSE = ( '', 'VAMPIRE',    'LICH', 'WEREWOLF', 'DALAHAN', 'ZOMBIE', 
    'GHOST', 'POSESSED')
TEMPER_TYPES = ('HERO', 'GENKI',    'YANDERE',  'TSUNDERE',
    'KUDERE',   'DERETSUN', 'TSUNTSUN', 'DANDERE',  'TOMBOY',
    'BISHOJO')
