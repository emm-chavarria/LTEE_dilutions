from opentrons import protocol_api       

metadata = {
	'apiLevel': '2.12',
    'protocolName': 'LTEE daily dilutions',
    'author': 'Emmanuel Chavarria',
    'description':'Transfer 2ul liquid after 24 hrs incubation into 198ul of fresh medium every 24 hrs'}


def run(protocol: protocol_api.ProtocolContext):

    # define deck positions and labware
    # tips
    tips300 = protocol.load_labware('opentrons_96_tiprack_300ul', 10)	#In slot 10
    tips10 = protocol.load_labware('opentrons_96_tiprack_10ul', 11) #in slot 11

    # load pipettes
    p300 = protocol.load_instrument('p300_single',mount='right',tip_racks=[tips300])
    p20 = protocol.load_instrument('p10_single', mount= 'left', tip_racks=[tips10])

    # plates
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 3)	#In slot 3

    # regents
    reagents = protocol.load_labware('opentrons_6_tuberack_falcon_50ml_conical', 6) # In slot 6
    dm25 = reagents['B1']   #50-ml falcon tube wtih dm25
    # p300.well_bottom_clearance.aspirate = 80 # 80 mm above bottom of falcon tube or ~40ml


# To start, manually load 200ul of culture in row 1.
# Add 20 ml of DM25 in 50-ml tube @ slot 7 well A1
# The robot then will transfer 1/100 daily into fresh dm25

# day 0
    # p300.well_bottom_clearance.aspirate = 15    # Position pipette to avoid dunking in 50-ml falcon tube with 20ml
    # # fresh medium
    # p300.distribute(198, dm25, plate.rows_by_name()['B'], disposal_volume=30)    # Transfer 198ul of fresh dm25 in new row
   
    # # inoculate
    # p20.transfer(2, plate.rows_by_name()['A'], plate.rows_by_name()['B'], # Transfer 2ul from A1 to B1, A2 to B2, A3 to B3, etc.
    #     new_tip='always', # Picks up a new tip everytime
    #     touch_tip=True)   # touch well sidewall due to small volume dispensed
   
    # # mixing all wells in row B after inoculation
    # p300.well_bottom_clearance.aspirate = 2    # reposition pipette for mixing wells in plate
    # wells = plate.rows_by_name()['B']
    # for i in wells:
    #     p300.pick_up_tip()
    #     p300.mix(3, 100, i)     
    #     p300.blow_out() # expel droplets from pipette after mixing
    #     p300.drop_tip()
    #     # mix_after=(5,19)) # Mix well after inoculation
    #     # blow_out=False, 
    #     # blowout_location='destination well') # Blow out pipette tip in inoculated well
    
    # # incubate for 24 hrs
    # # protocol.pause('Delay after this')
    protocol.delay(minutes=18*60, seconds=0) # incubate for 24 hrs

# day 1
    p300.well_bottom_clearance.aspirate = 15    # Position pipette to avoid dunking in 50-ml falcon tube with 20ml
    p300.distribute(198, dm25, plate.rows_by_name()['C'], disposal_volume=30)    # Transfer 198ul of fresh dm25 in new row
   
    p20.transfer(2, plate.rows_by_name()['B'], plate.rows_by_name()['C'], # Transfer 2ul from A1 to B1, A2 to B2, A3 to B3, etc.
        new_tip='always', # Picks up a new tip everytime
        touch_tip=True,   # touch well sidewall due to small volume dispensed
        blow_out=True, 
        blowout_location='destination well') # Blow out pipette tip in inoculated well

    # mixing all wells in row C after inoculation
    p300.well_bottom_clearance.aspirate = 2    # reposition pipette for mixing wells in plate
    wells = plate.rows_by_name()['C']
    for i in wells:
        p300.pick_up_tip()
        p300.mix(3, 100, i) 
        p300.blow_out() # expel droplets from pipette after mixing    
        p300.drop_tip()

# incubate for 24 hrs
    # protocol.pause('Delay after this')
    protocol.delay(minutes=24*60, seconds=0) # incubate for 24 hrs

# day 2
    p300.well_bottom_clearance.aspirate = 15    # Position pipette to avoid dunking in 50-ml falcon tube with 20ml
    p300.distribute(198, dm25, plate.rows_by_name()['D'], disposal_volume=30)    # Transfer 198ul of fresh dm25 in new row
   
    p20.transfer(2, plate.rows_by_name()['C'], plate.rows_by_name()['D'], # Transfer 2ul from A1 to B1, A2 to B2, A3 to B3, etc.
        new_tip='always', # Picks up a new tip everytime
        touch_tip=True,   # touch well sidewall due to small volume dispensed
        blow_out=True, 
        blowout_location='destination well') # Blow out pipette tip in inoculated well

    # mixing all wells in row D after inoculation
    p300.well_bottom_clearance.aspirate = 2    # reposition pipette for mixing wells in plate
    wells = plate.rows_by_name()['D']
    for i in wells:
        p300.pick_up_tip()
        p300.mix(3, 100, i) 
        p300.blow_out() # expel droplets from pipette after mixing    
        p300.drop_tip()

# incubate for 24 hrs
    # protocol.pause('Delay after this')
    protocol.delay(minutes=24*60, seconds=0) # incubate for 24 hrs

# day 3
    p300.well_bottom_clearance.aspirate = 15    # Position pipette to avoid dunking in 50-ml falcon tube with 20ml
    # fresh medium
    p300.distribute(198, dm25, plate.rows_by_name()['E'], disposal_volume=30)    # Transfer 198ul of fresh dm25 in new row
   
    # inoculate
    p20.transfer(2, plate.rows_by_name()['D'], plate.rows_by_name()['E'], # Transfer 2ul from A1 to B1, A2 to B2, A3 to B3, etc.
        new_tip='always', # Picks up a new tip everytime
        touch_tip=True)   # touch well sidewall due to small volume dispensed
   
    # mixing all wells in row B after inoculation
    p300.well_bottom_clearance.aspirate = 2    # reposition pipette for mixing wells in plate
    wells = plate.rows_by_name()['E']
    for i in wells:
        p300.pick_up_tip()
        p300.mix(3, 100, i)     
        p300.blow_out() # expel droplets from pipette after mixing
        p300.drop_tip()
        # mix_after=(5,19)) # Mix well after inoculation
        # blow_out=False, 
        # blowout_location='destination well') # Blow out pipette tip in inoculated well
    
    # incubate for 24 hrs
    # protocol.pause('Delay after this')
    protocol.delay(minutes=24*60, seconds=0) # incubate for 24 hrs