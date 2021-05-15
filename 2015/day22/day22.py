#!/usr/bin/env python

from collections import namedtuple

Spell = namedtuple(
    "Spell", ["name", "cost", "damage", "heal", "armor", "mana", "duration"]
)


all_spells = [
    Spell(name="Magic Missile", cost=53, damage=4, heal=0, armor=0, mana=0, duration=1),
    Spell(name="Drain", cost=73, damage=2, heal=2, armor=0, mana=0, duration=1),
    Spell(name="Shield", cost=113, damage=0, heal=0, armor=7, mana=0, duration=6),
    Spell(name="Poison", cost=173, damage=3, heal=0, armor=0, mana=0, duration=6),
    Spell(name="Recharge", cost=229, damage=0, heal=0, armor=0, mana=101, duration=5),
]

CastedSpell = namedtuple("CastedSpell", ["spell", "duration"])


def battle(
    player_turn: bool,
    player_health: int,
    player_mana: int,
    casted_spells: list[CastedSpell],
    boss_health: int,
    boss_damage: int,
    mana_spent: int,
    hard_mode=False,
    best_mana_spent: int = float("inf"),
):

    player_damage = sum(casted_spell.spell.damage for casted_spell in casted_spells)
    player_armor = sum(casted_spell.spell.armor for casted_spell in casted_spells)
    player_health += sum(casted_spell.spell.heal for casted_spell in casted_spells)
    player_mana += sum(casted_spell.spell.mana for casted_spell in casted_spells)

    casted_spells = list(
        filter(
            lambda casted_spell: casted_spell.duration > 0,
            map(
                lambda casted_spell: CastedSpell(
                    casted_spell.spell, casted_spell.duration - 1
                ),
                casted_spells,
            ),
        )
    )

    boss_health -= player_damage
    if boss_health <= 0:
        return mana_spent

    if player_turn:
        if hard_mode:
            player_health -= 1
            if player_health <= 0:
                return None
        casted_spells_ = [casted_spell.spell for casted_spell in casted_spells]
        allowed_spells = filter(lambda spell: spell not in casted_spells_, all_spells)
        affordable_spells = filter(
            lambda spell: spell.cost <= player_mana, allowed_spells
        )
        for spell in affordable_spells:
            new_mana_spent = mana_spent + spell.cost
            new_player_mana = player_mana - spell.cost
            if new_mana_spent > best_mana_spent:
                continue
            result = battle(
                False,
                player_health,
                new_player_mana,
                casted_spells + [CastedSpell(spell, spell.duration)],
                boss_health,
                boss_damage,
                new_mana_spent,
                hard_mode,
                best_mana_spent,
            )
            if result:
                best_mana_spent = min(result, best_mana_spent)
        return best_mana_spent
    else:
        player_health -= max(boss_damage - player_armor, 1)
        if player_health <= 0:
            return None
        return battle(
            True,
            player_health,
            player_mana,
            casted_spells,
            boss_health,
            boss_damage,
            mana_spent,
            hard_mode,
            best_mana_spent,
        )


def part1():
    return battle(True, 50, 500, [], 51, 9, 0)


def part2():
    return battle(True, 50, 500, [], 51, 9, 0, True)


print("Part 1:", part1())
print("Part 1:", part2())
